from django.db import models

# Create your models here.
from datetime import timedelta
from decimal import Decimal as D
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel
from utils.abstract_models import (AbstractTitleModel, AbstractDateTimeModel,
                                   AbstractTitleAndActivatorModel, AbstractActivatorModel)

# Create your models here.
User = get_user_model()


def verify_event_and_sub_event(event_obj, sub_event_obj):
    """here we are mathing the event child"""
    if sub_event_obj not in event_obj.sub_events.all():
        raise ValidationError(f"{sub_event_obj} in not part of {event_obj}")


class EventType(AbstractTitleAndActivatorModel):
    """event type model"""

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        if self.title.lower() == "other":
            raise ValidationError("Other object is not deletable.")
        return super(EventType, self).delete(using, keep_parents)


class Relation(AbstractTitleAndActivatorModel):
    """Event relation"""

    def __str__(self):
        return self.title


class Event(AbstractTitleModel, AbstractDateTimeModel):
    """user event models"""

    class EventStatus(models.TextChoices):
        """event status enum"""
        IN_REVIEW = "in_review", "In Review"
        ACTIVE = "active", "Active"
        COMPLETED = 'completed', "Completed"
        CANCELLED = "cancelled", "Cancelled"
        PENDING = "pending", "Pending"
    EventStatus=

    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name="ty_events")
    relation = models.ForeignKey(Relation,
                                 help_text="show us the relation of event creator",
                                 on_delete=models.CASCADE, related_name="rel_events")

    status = models.CharField(choices=EventStatus.choices, max_length=15, default=EventStatus.PENDING)
    advance_amount = models.DecimalField(default=D(0.0), decimal_places=2, max_digits=9)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    is_paid = models.BooleanField(default=False, help_text="check is advanced amount is paid or not")
    total_invitation = models.IntegerField(default=0,
                                           help_text="is just for the record to get just idea"
                                                     " of how many invitees are coming")
    employee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="employee_events")
    closure_date = models.DateField(help_text="date of when the event is completed", null=True, blank=True)
    register_date = models.DateField(help_text="date of when the event going to occur")
    approval_date = models.DateTimeField(help_text="date time of when the event is approved", null=True, blank=True)
    linked_event = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name="linked_events")
    other_event_type_title = models.CharField(max_length=30, null=True, blank=True,
                                              help_text="incase if the other type of the"
                                                        " event type is we have then we store here that name")

    def __str__(self):
        return f"{self.title} - {self.user} - {self.status}"

    @classmethod
    def allowed_cancellation_status(cls):
        """status list that allow event to be cancelled"""
        return [cls.EventStatus.IN_REVIEW, cls.EventStatus.ACTIVE, cls.EventStatus.PENDING]

    @property
    def event_type_title(self):
        event_type_title = self.event_type.title
        if not event_type_title.lower() == "other":
            return event_type_title
        return self.other_event_type_title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """restrict to allow self relations"""
        if self.linked_event and self.linked_event.pk == self.pk:
            raise ValidationError("You can not link same event.")
        super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        if self.register_date and self.register_date < timezone.now().date():
            raise ValidationError({"register_date": "register date must be greater then today."})

    def get_daily_notification_message(self):
        current_time = timezone.now()
        sub_events_titles_list = self.sub_events.filter(event_date=current_time).values_list("title", flat=True)
        sub_events_titles = ", ".join(sub_events_titles_list)
        return f"You have to attend today " + sub_events_titles


class SubEvent(AbstractTitleModel):
    """ sub event model,
        This model is related to the Main Event model,
        model represent  the if the event have their different type of venue and address

        NOTE: as of now we have only one hierarchy sub event
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="sub_events")
    event_date = models.DateField(help_text="date of when the sub event going to happen")
    start_time = models.TimeField()
    end_time = models.TimeField()
    end_date = models.DateField(null=True)
    venue = models.CharField(max_length=150, help_text="venue for the event")
    address = models.TextField()
    city = models.CharField(max_length=50)
    country = CountryField()
    postal_code = models.IntegerField(null=True)
    is_common = models.BooleanField(default=False, help_text="decide that is a common to linked event.")

    def __str__(self):
        return f"{self.title}- is common {self.is_common}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SubEvent, self).save(*args, **kwargs)

    def clean(self):
        if self.event_date and self.event_date < timezone.now().date() + timedelta(days=1):
            raise ValidationError({"event_date":"date must be greater then today"})
        is_time_set = self.start_time and self.end_time
        if is_time_set and self.start_time >= self.end_time:
            raise ValidationError({"start_time": "Start time must be greater then the end time."})


class UserEvent(models.Model):
    """
    user event model
    here we can identify or get the information
    how many people are invited
    how many people are confirmed
    """

    class AttendanceChoice(models.TextChoices):
        """Attendance Enum"""
        ATTENDING = "attending", "Attending"
        KIV = "kiv", "KIV"
        NOT_ATTENDING = "not_attending", "Not attending"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_events")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="user_events")
    sub_event = models.ForeignKey(SubEvent, on_delete=models.CASCADE, related_name="user_sub_events")
    is_notify = models.BooleanField(default=True)
    attendance = models.CharField(choices=AttendanceChoice.choices, max_length=15)

    class Meta:
        unique_together = [['user', 'event', "sub_event"]]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.event and self.sub_event:
            verify_event_and_sub_event(self.event, self.sub_event)
        super().save(force_insert, force_update, using, update_fields)


class EventHost(AbstractActivatorModel):
    """
    Event host model

    show us who is going to host the event,
    basically two type( 1 : owner ,2 : CO-host)
    Co-host: is when the use is not registered in the OUR invitee app
    owner : is when the user is already registered into the picture

    if CO-host register into the app then we also show them to Event related data

    """

    class HostTypeChoices(models.TextChoices):
        """host type choices"""
        OWNER = "owner", "Owner"
        CO_HOST = "co_host", "Co-host"

    email = models.EmailField()
    phone = PhoneNumberField()
    event_host_type = models.CharField(choices=HostTypeChoices.choices, max_length=10)
    is_deleted = models.BooleanField(default=False)

    # user is store when the email/phone is fields match with our exiting user
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="event_hosts")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="hosted_events")


class EventGreetings(models.Model):
    """event greeting or some special blessings"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_greetings")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_greetings")
    greetings = models.TextField(verbose_name="greeting/blessing")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class EventGift(models.Model):
    """this model is only for the record how many special gift, voucher and cash we collected on particulate Event"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="gift_records")
    cash_gift = models.DecimalField(default=D(0.0), decimal_places=2, max_digits=9)
    voucher_gift = models.DecimalField(default=D(0.0), decimal_places=2, max_digits=9)
    special_gift = models.DecimalField(default=D(0.0), decimal_places=2, max_digits=9)


class EventVoucher(models.Model):
    """event voucher"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="vouchers")
    voucher = models.ForeignKey("gift.Voucher", on_delete=models.CASCADE, related_name="event_vouchers")
    voucher_option = models.ForeignKey("gift.VoucherOption", on_delete=models.CASCADE,
                                       related_name="voucher_option_events")

    class Meta:
        unique_together = [['event', 'voucher', "voucher_option"]]

    @classmethod
    def create(cls, event, voucher, voucher_option):
        instance = cls(
            event=event,
            voucher=voucher,
            voucher_option=voucher_option
        )
        instance.save()
        return instance


class EventSpecialGift(models.Model):
    """event special gift"""
    special_gift = models.ForeignKey("gift.SpecialGift", on_delete=models.CASCADE, related_name="event_special")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="special_gifts")
    target = models.DecimalField(default=D(0.0), decimal_places=2, max_digits=9)
    collection = models.DecimalField(default=D(0.0), decimal_places=2, max_digits=9)

    def collection_percentage(self):
        """calculate how many percentage target is archived """
        float_target = float(self.target)
        float_collection = float(self.collection)
        try:
            return round(float_collection / float_target * 100, 2)
        except ZeroDivisionError:
            return 0.0

    class Meta:
        unique_together = [['event', 'special_gift']]


class UserAttendance(models.Model):
    """record we're storing that how many people are going to attend and what type of food venue they like"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendance")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_attendance")
    sub_event = models.ForeignKey(SubEvent, on_delete=models.CASCADE, related_name="sub_event_attendance")
    veg_count = models.IntegerField(default=0)
    non_veg_count = models.IntegerField(default=0)

    class Meta:
        unique_together = [['user', 'event', "sub_event"]]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.event and self.sub_event:
            verify_event_and_sub_event(self.event, self.sub_event)
        super().save(force_insert, force_update, using, update_fields)


class SoloChargeAndTax(SingletonModel):
    service_tax = models.FloatField(help_text="percentage of the service tax", default=1.3)
    service_charge = models.FloatField(help_text="percentage of the service charge", default=1.3)


def get_current_service_charge():
    change_and_tax = SoloChargeAndTax.get_solo()
    return change_and_tax.service_charge


def get_current_service_tax():
    change_and_tax = SoloChargeAndTax.get_solo()
    return change_and_tax.service_tax


class PaymentBreakUp(models.Model):
    """actually payment we are storing after the payment successful"""
    actual_amount = models.DecimalField(decimal_places=2, max_digits=9, default=D(0.0))
    service_tax = models.FloatField(help_text="current percentage of the service tax",
                                    default=get_current_service_tax)
    service_charge = models.FloatField(help_text="current percentage of the service charge",
                                       default=get_current_service_charge)
    excluded_tax_amount = models.DecimalField(decimal_places=2, max_digits=9, default=D(0.0))

    def excluded_tax_amount_cal(self):
        tax = float(self.service_charge) + float(self.service_tax)
        percentage = tax / 100
        difference_amount = round(float(self.actual_amount) * percentage, 2)
        str_amount = '{:.2f}'.format(round(float(self.actual_amount) - round(difference_amount, 2), 2))
        return D(str_amount)

    def save(self, *args, **kwargs):
        self.excluded_tax_amount = self.excluded_tax_amount_cal()
        super(PaymentBreakUp, self).save(*args, **kwargs)


class EventPayment(models.Model):
    """Pyment related data goes here"""

    class PaymentTypeChoices(models.TextChoices):
        """pyment types choices"""
        ADVANCE = 'advance', "Advance"
        CASH = 'cash', 'Cash'
        VOUCHER = 'voucher', 'Voucher'
        SPECIAL_GIFT = 'special_gift', 'Special gift'

    class EventPaymentStatuses(models.TextChoices):
        """payment status"""
        SUCCESS = "success"
        FAIL = "fail"
        IN_PROGRESS = "in_progress"

    # here we are set the event and user nullable True
    # because if we delete the Event or User then we just kept the Payment data for the record
    # we are going to always required from the CODE side
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="event_payments")
    payment_type = models.CharField(choices=PaymentTypeChoices.choices, max_length=15, db_index=True)
    breakup_amount = models.ForeignKey(PaymentBreakUp, on_delete=models.CASCADE, related_name="event_payments",
                                       null=True, blank=True)
    status = models.CharField(max_length=30, choices=EventPaymentStatuses.choices,
                              default=EventPaymentStatuses.IN_PROGRESS)
    comment = models.TextField(null=True, blank=True)  # optional
    date_paid = models.DateField(help_text="date of when amount is paid")
    event_vouchers = models.ManyToManyField(EventVoucher, null=True, blank=True, related_name="evnet_voucher_payments")
    event_special_gift = models.ForeignKey(EventSpecialGift, null=True, blank=True, on_delete=models.SET_NULL,
                                           related_name="special_gift_pyment")
    is_successful = models.BooleanField(default=False, db_index=True,
                                        help_text="after the payment gateway  successful payment make it True")
    transaction_id = models.CharField(max_length=100, null=True, blank=True
                                      , help_text="Transaction id from the pyment gateway")

    invoice_number = models.CharField(max_length=50, null=True, blank=True)
    fpx_seller_id = models.CharField(max_length=150, null=True, blank=True)
    fpx_transaction_msg = models.CharField(max_length=150, null=True, blank=True)

    @classmethod
    def is_allowed_to_daily_settlement(cls, payment_type):
        return cls.PaymentTypeChoices.CASH == payment_type

    @classmethod
    def final_amount_payment_types(cls):
        return [cls.PaymentTypeChoices.SPECIAL_GIFT.value, cls.PaymentTypeChoices.CASH.value]

    def generate_invoice_number(self):
        prefix = self.payment_type.replace("_", "")
        return f"{prefix}{self.id}".upper()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.event or not self.user:
            raise ValidationError("You are missing event or user data to enter.")
        if self.payment_type == self.PaymentTypeChoices.SPECIAL_GIFT and not self.event_special_gift:
            raise ValidationError("Please add event_special_gift instance")
        self.validate_unique_invoice_number()
        super().save(force_insert, force_update, using, update_fields)

    def validate_unique_invoice_number(self):
        qs = self.__class__.objects.filter(invoice_number__iexact=self.invoice_number)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Invoice Number is already exists.")

    @property
    def payment_type_detail(self):
        if not self.payment_type:
            return ""
        if self.payment_type == self.PaymentTypeChoices.CASH:
            return self.PaymentTypeChoices.CASH.value
        elif self.payment_type == self.PaymentTypeChoices.VOUCHER:
            voucher_titles = ",".join(self.event_vouchers.all().values_list("voucher__title", flat=True))
            return f"voucher - {voucher_titles}"
        return f"special_gift - {self.event_special_gift.special_gift.title}"


class UserScan(models.Model):
    """getting record after the UserScan"""
    user = models.ForeignKey(User, related_name="user_scans", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="user_scans", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class EventQR(AbstractDateTimeModel):
    """store event QR image"""
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="qr_code")
    image = models.ImageField(upload_to='event/qr-code')
    scan_count = models.IntegerField(default=0)

    def __str__(self):
        """return event title"""
        return self.event.title


class EventHistory(AbstractDateTimeModel):
    """store the event history with each and every task perform on Event"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="histories")
    action_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name="event_histories")
    # in reasons, we are not sure how many reason are going to be there so as of now make default char, and
    # we can handle this by ENUM manually
    cancellation_reasons = models.CharField(null=True, blank=True, max_length=30, default="")
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        sort_description = self.comment or self.cancellation_reasons or ""
        return f"{self.event}, -- {sort_description[:15]}.. "


class EventAttendingQR(models.Model):
    """store QR code to use when invitees are going to attend """
    event = models.ForeignKey(Event, related_name="event_attending_qr", on_delete=models.CASCADE)
    sub_event = models.ForeignKey(SubEvent, related_name="sub_event_attending_qr", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="event/attending-qr")
    attending_count = models.IntegerField(default=0)

    class Meta:
        unique_together = [['event', "sub_event"]]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.event and self.sub_event:
            verify_event_and_sub_event(self.event, self.sub_event)
        super().save(force_insert, force_update, using, update_fields)


def event_upload_dir(event_image_instance, filename):
    """use to store the images with the event upload"""
    return f"event/event_{event_image_instance.event.id}/{filename}"


class EventImages(models.Model):
    image = models.ImageField(upload_to=event_upload_dir)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_images")
