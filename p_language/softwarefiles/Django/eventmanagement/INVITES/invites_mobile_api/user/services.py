"""services contain model related helper fuction """
import logging
import boto3
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import MultipleObjectsReturned
from django_otp import devices_for_user
from rest_framework.authtoken.models import Token
from .models import SMSDevice, BankDetail, Card
from .constants import DeviceType
from event.services import get_events, get_user_scans
from event.models import EventPayment, UserEvent

User = get_user_model()

AWS_AUTH_PARAMS = {
    'aws_access_key_id': settings.AWS_ACCESS_KEY_ID,
    'aws_secret_access_key': settings.AWS_SECRET_ACCESS_KEY,
    'region_name': settings.AWS_DEFAULT_REGION
}


def get_client():
    """Get a client with which to send SMS"""
    if settings.DEBUG:
        logging.info("SMS Service: In testing mode")
        return TestClient()
    return boto3.client(
        "sns",
        **AWS_AUTH_PARAMS
    )


class TestClient:
    """Client to output sms to logs instead of sending"""

    @staticmethod
    def publish(PhoneNumber: str, Message: str):  # pylint: disable=invalid-name
        """Emulate the normal publish command, just out to logs"""

        log_message = f"SMS to {PhoneNumber}: {Message}"
        logging.info(log_message)


def get_users(**kwargs):
    """kwargs: accepts model related params"""
    return User.objects.filter(**kwargs)


def create_phone_device(user):
    """Create a Phone  device"""
    device = SMSDevice(user=user, name=DeviceType.PHONE.value, confirmed=False)
    device.save()
    return device


def create_email_device(user):
    """Create an email device"""
    device = SMSDevice(user=user, name=DeviceType.EMAIL.value, confirmed=False)
    device.save()
    return device


def get_user_phone_devices(user):
    """get user  phone devices list"""
    devices = devices_for_user(user, confirmed=None)
    return [device for device in devices if device.name == DeviceType.PHONE.value]


def get_user_phone_device(user):
    """return single phone device"""
    devices = get_user_phone_devices(user)
    if devices:
        return devices[0]
    return None


def get_user_email_devices(user):
    """get user  phone email list"""
    devices = devices_for_user(user, confirmed=None)
    return [device for device in devices if device.name == DeviceType.EMAIL.value]


def get_user_email_device(user):
    """return single email device"""
    devices = get_user_email_devices(user)
    if devices:
        return devices[0]
    return None


def validate_phone_token(user, token):
    """validate phone number token"""
    device = get_user_phone_device(user)
    if device:
        return device.verify_token(token), device
    return False, None


def validate_email_token(user, token):
    """validate email number token"""
    device = get_user_email_device(user)
    if device:
        return device.verify_token(token), device
    return False, None


def make_device_confirmed(device):
    """make sms device confirmed"""
    device.confirmed = True
    device.save()
    return device


def is_phone_confirmed(user):
    """verify is phone is confirmed device"""
    device = get_user_phone_device(user)
    if device:
        return device.confirmed
    return False


def is_email_confirmed(user):
    """verify is phone is confirmed device"""
    device = get_user_email_device(user)
    if device:
        return device.confirmed
    return False


def get_or_create_auth_token(user):
    """user auth token to """
    token = Token.objects.get_or_create(user=user)[0]
    return token.key


def mark_device_unconfirmed(device):
    """make user device to unconfirmed"""
    device.confirmed = False
    device.save()
    return device


def get_user_bank_details(user):
    """return user bank detail queryset"""
    return BankDetail.objects.filter(user=user)


def get_user_cards(user):
    """get user cards"""
    return Card.objects.filter(user=user)


def get_user_by_phone(phone):
    """ get event by id"""
    try:
        return User.objects.get(phone=phone)
    except User.DoesNotExist:
        return None


def get_user_by_email(email: str):
    """ get event by id"""
    user = User.objects.filter(email=email).first()
    return user


def send_sms(phone, message):
    from utils.fire_work import send_sms_request
    send_sms_request(phone, message)


def normalize_email(email):
    """
    Normalize the email address by lowercasing .
    """
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = email_name + '@' + domain_part.lower()
    return email.lower()


def get_dash_board_report(user):
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
