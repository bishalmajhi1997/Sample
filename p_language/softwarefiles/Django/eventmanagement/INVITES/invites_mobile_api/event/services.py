"""event model services"""
import logging
import pdfkit
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal as D
from io import BytesIO
import qrcode
from django.core.files import File
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count, Q
from django_rq import job
from notifications.signals import notify
from rest_framework.serializers import ModelSerializer, ValidationError
from gift.services import get_voucher_option_by_voucher_id
from utils.helpers import convert_base64_string
from .constants import EventCancellationChoices, WEEKLY_EVENT_NOTIFICATION_MESSAGE, THREE_DAY_EVENT_NOTIFICATION_MESSAGE
from .models import (Event, SubEvent, UserEvent, EventType, Relation,
                     EventHost, UserAttendance, EventGreetings, EventVoucher, EventSpecialGift, EventQR, EventHistory,
                     EventGift, EventPayment, EventAttendingQR, EventImages, UserScan)


# TODO:created here because of circular imports
class UserDataSerializer(ModelSerializer):
    """serializer to use to get image path and common data"""

    class Meta:
        model = get_user_model()
        fields = ["id", 'first_name', 'last_name', "image"]


def get_events(**kwargs):
    """filter the events"""
    return Event.objects.filter(**kwargs)


def get_user_events_and_hosted_events(user):
    """here we include also hosted events"""
    # EventHost.
    query_set = Q(Q(user=user) | Q(hosted_events__user=user) | Q(user_scans__user=user))
    events_ids = Event.objects.filter(query_set).values_list("id", flat=True)
    return Event.objects.filter(pk__in=set(events_ids))


def get_sub_events(**kwargs):
    """filter the events"""
    return SubEvent.objects.filter(**kwargs)


def get_relations(**kwargs):
    """filter the events"""
    return Relation.objects.filter(**kwargs)


def get_event_types(**kwargs):
    """filter the events"""
    return EventType.objects.filter(**kwargs)


def get_sub_event(sub_evnet_id: int):
    """ get event by id"""
    try:
        return SubEvent.objects.get(id=sub_evnet_id)
    except SubEvent.DoesNotExist:
        return None


def get_user_events(**kwargs):
    """get filter query set of UserEvent model"""
    return UserEvent.objects.filter(**kwargs)


def create_or_update_user_event(event, sub_event, user, attendance):
    user_event_data = {
        "event": event,
        "sub_event": sub_event,
        "user": user,
    }
    user_event = get_user_events(**user_event_data).first()
    if attendance == UserEvent.AttendanceChoice.NOT_ATTENDING:
        user_attendances = get_user_attendances(**user_event_data)
        user_attendances.update(veg_count=0, non_veg_count=0)
    user_event_data["attendance"] = attendance
    if not user_event:
        return UserEvent.objects.create(**user_event_data)
    UserEvent.objects.filter(pk=user_event.pk).update(**user_event_data)
    return user_event


def create_or_update_user_attendance(validated_data: dict):
    user_attendance_data = {
        "event": validated_data.get('event'),
        "sub_event": validated_data.get('sub_event'),
        "user": validated_data.get('user'),
    }
    user_attendance = get_user_attendances(**user_attendance_data).first()
    if not user_attendance:
        return UserAttendance.objects.create(**validated_data)
    UserAttendance.objects.filter(pk=user_attendance.pk).update(**validated_data)
    user_attendance.refresh_from_db()
    return user_attendance


def get_excluded_common_sub_events(event: Event):
    """combine the event and linked events sub events"""
    main_event_sub_events = event.sub_events.all()
    linked_event = event.linked_event
    if linked_event:
        linked_event_sub_events = linked_event.sub_events.filter(is_common=False)
        return main_event_sub_events | linked_event_sub_events
    return main_event_sub_events


def get_event_host_with_phone_number_if_user_none(phone_number):
    """get event host QS with phone number where user is None"""
    return EventHost.objects.filter(user=None, phone=phone_number)


def assign_user_to_event_host(user_obj, event_host_obj):
    """assign the user to event host object"""
    event_host_obj.user = user_obj
    event_host_obj.save()
    return event_host_obj


def get_event_hosts(**kwargs):
    """event host filtered QS"""
    return EventHost.objects.filter(**kwargs)


def get_event_special_gifts(**kwargs):
    """return event special gifts"""
    return EventSpecialGift.objects.filter(**kwargs)


def get_events_vouchers(**kwargs):
    """get events vouchers QS"""
    return EventVoucher.objects.filter(**kwargs)


def get_user_attendances(**kwargs):
    """return the user attendance QS"""
    return UserAttendance.objects.filter(**kwargs)


def get_event_greetings(**kwargs):
    """get user event greetings"""
    return EventGreetings.objects.filter(**kwargs)


def create_qr_code_by_event(event_obj):
    """create QR code by event """
    img = qrcode.make(convert_base64_string(f'event_id={event_obj.id};'
                                            f'event_title={event_obj.title};user={event_obj.user.first_name}'))
    stream = BytesIO()
    img.save(stream)
    event_qr = EventQR(event=event_obj)
    file_name = f"event_{event_obj.id}.png"
    event_qr.image.save(file_name, File(stream), save=False)
    event_qr.save()
    return event_qr


def create_attending_qr_code_by_event_and_sub_event(event_obj, sub_event):
    """create attending QR code by event  and sub event"""
    img = qrcode.make(f'event_id={event_obj.id};sub_event={sub_event.id}')
    stream = BytesIO()
    img.save(stream)
    attending_event_qr = EventAttendingQR(event=event_obj, sub_event=sub_event)
    file_name = f"event_{event_obj.id}_{sub_event.id}.png"
    attending_event_qr.image.save(file_name, File(stream), save=False)
    attending_event_qr.save()
    return attending_event_qr


def get_event_qrs(**kwargs):
    """return QR codes"""
    return EventQR.objects.filter(**kwargs)


def get_event_attending_qrs(**kwargs):
    """return attending QR codes"""
    return EventAttendingQR.objects.filter(**kwargs)


def update_attending_scan_count(event_id, sub_event_id):
    """update the attending scan count based on event id"""
    event_qr = EventAttendingQR.objects.get(event_id=event_id, sub_event_id=sub_event_id)
    event_qr.attending_count += 1
    event_qr.save(update_fields=["attending_count"])


def update_event_status(event, event_status: Event.EventStatus):
    """update the event status"""
    event.status = event_status
    event.save(update_fields=["status"])
    return event


def event_cancellation_history(user, event, comment, cancellation_reasons):
    """create cancellation history"""
    history_obj = create_history_for_event(user, event, comment)
    history_obj.cancellation_reasons = cancellation_reasons
    history_obj.save(update_fields=["cancellation_reasons"])


def create_history_for_event(user, event, comment):
    """create event history"""
    event_history = EventHistory(action_by=user, event=event, comment=comment)
    event_history.save()
    return event_history


def assign_employee_to_event(event, employee_user):
    """assign employees after the event action, so we can identify which user performed last action"""
    event.employee = employee_user
    event.save(update_fields=["employee"])


def attend_event_request(user, event):
    """attend event request """
    assign_employee_to_event(event, user)
    update_event_status(event, Event.EventStatus.IN_REVIEW)


def generate_sales_employees_analytics(user):
    """
     here we are generating the analytics of the sales person
     like how many event he cancelled and how many are they have attended
    """
    context = {
        "success_rate": {
            "success": 0,
            "cancelled": 0,
            "total": 0,
        },
        "unsuccessful_rate": {
            "payment_concern": 0,
            "duplicate_request": 0,
            "fraud_request": 0,
            "just_enquiry": 0,

        },
    }
    employees_current_events = Event.objects.filter(employee=user)
    user_event_history = EventHistory.objects.filter(action_by=user)
    cancel_duplicate_request = user_event_history.filter(
        cancellation_reasons__icontains=EventCancellationChoices.DUPLICATE_REQUEST).count()
    cancel_fraud_request = user_event_history.filter(
        cancellation_reasons__icontains=EventCancellationChoices.FRAUD_REQUEST).count()
    cancel_just_enquiry = user_event_history.filter(
        cancellation_reasons__icontains=EventCancellationChoices.JUST_ENQUIRY).count()
    cancel_payment_concern = user_event_history.filter(
        cancellation_reasons__icontains=EventCancellationChoices.PAYMENT_CONCERN).count()
    cancelled_event_sum = sum([cancel_payment_concern, cancel_just_enquiry,
                               cancel_fraud_request, cancel_duplicate_request])

    context['success_rate']['success'] = abs(employees_current_events.count() - cancelled_event_sum)
    context['success_rate']['cancelled'] = cancelled_event_sum
    context['success_rate']['total'] = employees_current_events.count()
    context['unsuccessful_rate']['duplicate_request'] = cancel_duplicate_request
    context['unsuccessful_rate']['fraud_request'] = cancel_fraud_request
    context['unsuccessful_rate']['just_enquiry'] = cancel_just_enquiry
    context['unsuccessful_rate']['payment_concern'] = cancel_payment_concern

    return context


def get_event_history(**kwargs):
    """history data QS"""
    return EventHistory.objects.filter(**kwargs)


def update_scan_count(event_id):
    """update the scan count based on event id"""
    event_qr = EventQR.objects.get(event_id=event_id)
    event_qr.scan_count += 1
    event_qr.save(update_fields=["scan_count"])


def event_attendance_report_with_sub_event_id_and_user(sub_event_id):
    sub_event_obj = SubEvent.objects.get(id=sub_event_id)
    event = sub_event_obj.event
    total_invitation = event.total_invitation
    scan_count = event.qr_code.scan_count if hasattr(event, "qr_code") else 0
    non_veg_sum = Sum("non_veg_count")
    veg_sum = Sum("veg_count")
    user_attendances = get_user_attendances(sub_event=sub_event_obj)
    user_attendances_counts = user_attendances.aggregate(
        veg_count=veg_sum, non_veg_count=non_veg_sum)
    attending_count = Count('attendance', filter=Q(attendance="attending"))
    kiv_count = Count('attendance', filter=Q(attendance="kiv"))
    not_attending_count = Count('attendance', filter=Q(attendance="not_attending"))
    user_events = get_user_events(sub_event=sub_event_obj)
    user_events_counts = user_events.aggregate(
        attending=attending_count, kiv=kiv_count, not_attending=not_attending_count
    )
    return {
        "scan_count": scan_count,
        "total_invitation": total_invitation,
        "no_response_count": abs(scan_count - user_events.count()),
        "food_count": user_attendances_counts,
        "attendance": user_events_counts
    }


def sub_event_user_attendance_report(sub_event_id, request):
    user_attendances = get_user_attendances(sub_event_id=sub_event_id)
    attendance_list = []

    for each_attendance in user_attendances:
        attendance_data = dict()
        user_event = get_user_events(event=each_attendance.event, user=each_attendance.user,
                                     sub_event=each_attendance.sub_event).first()
        attendance_data["status"] = user_event.attendance if user_event else "No status found."
        user = each_attendance.user
        attendance_data["user"] = UserDataSerializer(instance=user, context={"request": request}).data
        attendance_data["veg_count"] = each_attendance.veg_count
        attendance_data["non_veg_count"] = each_attendance.non_veg_count
        attendance_list.append(attendance_data)
    return attendance_list


def generate_overall_event_gift_report(event_id):
    """report that give us overall received gift payments"""
    event_gift = EventGift.objects.filter(event_id=event_id).first()
    if not event_gift:
        return {"message": "No report found."}
    overall_report_dict = {
        "cash_gift": event_gift.cash_gift,
        "voucher_gift": event_gift.voucher_gift,
        "special_gift": event_gift.special_gift,
        "advance_amount": event_gift.event.advance_amount,
    }
    return overall_report_dict


def detailed_gift_report_from_payment(event_id, request):
    event_payments = EventPayment.objects.filter(
        event_id=event_id,
        status=EventPayment.EventPaymentStatuses.SUCCESS, is_successful=True). \
        exclude(payment_type=EventPayment.PaymentTypeChoices.ADVANCE)
    detailed_report_list = []
    for each_payment in event_payments:
        detailed_report_dict = dict()
        detailed_report_dict["payment_type"] = each_payment.payment_type_detail
        detailed_report_dict["user"] = UserDataSerializer(instance=each_payment.user, context={"request": request}).data
        detailed_report_dict["amount"] = each_payment.breakup_amount.actual_amount \
            if each_payment.breakup_amount else D(0.0)
        detailed_report_list.append(detailed_report_dict)
    return detailed_report_list


def get_event_images(**kwargs):
    """return Event images QS"""
    return EventImages.objects.filter(**kwargs)


def user_hosted_events(user):
    """here we're filtering the hosted events"""
    events = []
    for each_event_host in user.event_hosts.all():
        events.append(each_event_host.event)
    return events


def create_event_vouchers(event, voucher):
    event_vouchers = []
    for each_options in get_voucher_option_by_voucher_id(voucher.id):
        event_voucher_obj = get_events_vouchers(voucher=voucher,
                                                voucher_option=each_options,
                                                event=event).first()
        if not event_voucher_obj:
            event_voucher_obj = EventVoucher.create(
                voucher=voucher,
                voucher_option=each_options,
                event=event
            )
        event_vouchers.append(event_voucher_obj)
    return event_vouchers


def create_event_special_gifts(event, special_gift, target):
    event_special_gift_obj = get_event_special_gifts(event=event, special_gift=special_gift).first()
    if not event_special_gift_obj:
        event_special_gift_obj = EventSpecialGift(event=event, special_gift=special_gift, target=target)
        event_special_gift_obj.save()
        return event_special_gift_obj
    event_special_gift_obj.target = target
    event_special_gift_obj.save(update_fields=["target"])
    return event_special_gift_obj


def get_user_scans(**kwargs):
    """user scans"""
    return UserScan.objects.filter(**kwargs)


def crate_user_scan(user_id, event_id):
    get_user_model().objects.get(pk=user_id)  # the only sanity check for raising the proper error
    user_scan = UserScan(user_id=user_id, event_id=event_id)
    user_scan.save()
    return user_scan


def is_already_scan(user_id, event_id):
    user = get_user_model().objects.get(pk=user_id)
    event_user = Event.objects.get(pk=event_id).user
    if event_user == user:
        raise ValidationError({"error": "You can't scan you own event."})
    return UserScan.objects.filter(user_id=user_id, event_id=event_id).exists()


def user_dash_board_report(user):
    current_time = timezone.now()
    last_30_day = current_time - timedelta(days=30)
    next_30_day = current_time + timedelta(days=30)
    user_last_30_day_received_events = get_user_scans(user=user, created_at__lt=current_time,
                                                      created_at__gt=last_30_day).count()

    own_events = get_events(user=user).count()
    user_events = UserEvent.objects.filter(user=user, attendance=UserEvent.AttendanceChoice.ATTENDING)
    user_attended_event_last_30_day = user_events.filter(event__closure_date__lt=current_time.date(),
                                                         event__closure_date__gt=last_30_day.date(), ).count()
    user_up_coming_event_in_30_day = user_events.filter(event__closure_date__gt=current_time.date(),
                                                        event__closure_date__lt=next_30_day).count()
    gift_presents_last_30_days = EventPayment.objects.filter(user=user,
                                                             status=EventPayment.EventPaymentStatuses.SUCCESS,
                                                             date_paid__lt=current_time.date(),
                                                             date_paid__gt=last_30_day).count()
    return {
        "user_last_30_day_received_events": user_last_30_day_received_events,
        "own_events": own_events,
        "user_attended_event_last_30_day": user_attended_event_last_30_day,
        "user_skipped_event_last_30_day": user_last_30_day_received_events - user_attended_event_last_30_day,
        "user_up_coming_event_in_30_day": user_up_coming_event_in_30_day,
        "gift_presents_last_30_days": gift_presents_last_30_days
    }


def get_pdb_report_context(event_id):
    event_greeting = EventGreetings.objects.filter(event_id=event_id)
    event_payments = EventPayment.objects.filter(event_id=event_id, status=EventPayment.EventPaymentStatuses.SUCCESS)
    return {
        "greetings": event_greeting,
        "event_payments": event_payments
    }


def get_event_payments(**kwargs):
    return EventPayment.objects.filter(**kwargs)


def get_or_create_event_hosts(event_host_validate_data: dict):
    from user.services import get_user_by_phone, get_user_by_email
    event_host = EventHost.objects.filter(**event_host_validate_data).first()
    if not event_host:
        event_host = EventHost.objects.create(**event_host_validate_data)
        user = get_user_by_phone(event_host.phone) or get_user_by_email(event_host.email)
        if user:
            event_host.user = user
            event_host.save(update_fields=["user"])
    return event_host


def get_today_user_events():
    current_time = timezone.now()
    today_events = UserEvent.objects.filter(sub_event__event_date=current_time.date())
    return today_events


def get_user_after_3_day_events():
    after_3_day = timezone.now() + timedelta(days=2)
    upcoming_3_days_events = UserEvent.objects.filter(sub_event__event_date=after_3_day)
    return upcoming_3_days_events


def get_user_upcoming_week_events():
    tomorrow = timezone.now() + timedelta(days=1)
    next_6_day = tomorrow + timedelta(days=6)
    upcoming_events_in_week = UserEvent.objects.filter(
        sub_event__event_date__gte=tomorrow,
        sub_event__event_date__lt=next_6_day)
    return upcoming_events_in_week


def send_notifications_for_events():
    # .values("user").annotate(event_counts=Count("sub_event"))
    current_time = timezone.now()
    after_3_day = timezone.now() + timedelta(days=2)
    today_events = get_today_user_events()
    today_event__user_ids = today_events.values_list("user", flat=True)
    after_3_day_events = get_user_after_3_day_events().exclude(user__id__in=today_event__user_ids)
    upcoming_events_in_week = UserEvent.objects.none()
    if current_time.isoweekday() == 7:
        after_3_day_events_user_ids = after_3_day_events.values_list("user", flat=True)
        upcoming_events_in_week = get_user_upcoming_week_events().exclude(user__id__in=after_3_day_events_user_ids)
    for each_today in today_events.distinct("event", "user"):
        message = each_today.event.get_daily_notification_message()
        notify.send(each_today.user, recipient=each_today.user, verb=message)
    for each_3_day_event in after_3_day_events.values("user").annotate(event_counts=Count("sub_event")):
        user = get_user_model().objects.filter(pk=each_3_day_event.get("user")).first()
        if user:
            message = THREE_DAY_EVENT_NOTIFICATION_MESSAGE % (each_3_day_event.get("event_counts"), after_3_day)
            notify.send(user, recipient=user, verb=message)

    for each_week_event in upcoming_events_in_week.values("user").annotate(event_counts=Count("sub_event")):
        user = get_user_model().objects.filter(pk=each_week_event.get("user")).first()
        if user:
            message = WEEKLY_EVENT_NOTIFICATION_MESSAGE % each_week_event.get("event_counts")
            notify.send(user, recipient=user, verb=message)


def get_payment_pdf_context(event_id):
    event_payments = EventPayment.objects.filter(event_id=event_id, status=EventPayment.EventPaymentStatuses.SUCCESS)
    return {
        "event_payments": event_payments
    }


def get_greetings_pdf_context(event_id):
    event_greeting = EventGreetings.objects.filter(event_id=event_id)
    return {
        "greetings": event_greeting
    }


def get_summary_pdf_context(event_id):
    event_qr = EventQR.objects.filter(event_id=event_id).first()
    user_attendance = UserAttendance.objects.filter(event_id=event_id).first()
    user_event = UserEvent.objects.filter(event_id=event_id)
    attending_count = Count("user", filter=Q(attendance="attending"))
    not_attending_count = Count("user", filter=Q(attendance="not_attending"))
    user_counts = user_event.aggregate(attending_count=attending_count,
                                       not_attending_count=not_attending_count)
    return {
        "scan_count": event_qr.scan_count if event_qr else 0,
        "veg_count": user_attendance.veg_count if user_attendance else 0,
        "non_veg_count": user_attendance.non_veg_count if user_attendance else 0,
        "user_counts": user_counts,
    }


def get_pdf_templates_and_contexts_mapper(event_id):
    return [
        {"template_name": "event_summary.html",
         "context": get_summary_pdf_context(event_id),
         "file_name": "event_summary.pdf"},
        {"template_name": "event_greetings.html",
         "context": get_greetings_pdf_context(event_id),
         "file_name": "event_greetings_summary.pdf"},
        {"template_name": "event_payment_summary.html",
         "context": get_payment_pdf_context(event_id),
         "file_name": "event_payment_summary.pdf"},
    ]


def generate_attachments(event_id):
    attachments = []
    mime_type = 'application/pdf'
    for each_data in get_pdf_templates_and_contexts_mapper(event_id):
        pdf_response = get_pdf_str_response(each_data.get("template_name"), each_data.get("context"))
        attachments.append((each_data.get("file_name"), pdf_response, mime_type))
    return attachments


@job
def send_attachment_mail(event_id):
    event = Event.objects.get(pk=event_id)
    user = event.user
    body = "Here we attach the Final settlement report Files "
    mail = EmailMultiAlternatives(subject="Final settlement report", body=body,
                                  from_email="no-reply-dev@invites.com.my",
                                  to=[user.email],
                                  attachments=generate_attachments(event_id))
    mail.send()


def get_pdf_str_response(template_name, context):
    template_str = render_to_string(template_name, context)
    pdf_response = pdfkit.from_string(template_str)
    return pdf_response


def get_unique_event_voucher_by_event_id(event_id):
    event_vouchers = EventVoucher.objects.filter(event_id=event_id).values_list("event", "voucher")
    event_vouchers_uniques = list(set(event_vouchers))
    response_list = []
    for each_event, each_voucher in event_vouchers_uniques:
        unique_data = {"event": each_event, "voucher":each_voucher}
        response_list.append(unique_data)
    return response_list
