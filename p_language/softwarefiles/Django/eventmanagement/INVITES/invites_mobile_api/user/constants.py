"""user related constants or ENum"""
from enum import Enum
from django.conf import settings


class DeviceType(Enum):
    """Device Types for this user"""
    EMAIL = 'email'
    PHONE = 'phone'

    @classmethod
    def choices(cls):
        choices = [(constant.value, key) for key, constant in cls.__members__.items()]
        return choices



def get_default_email_password_params():
    DEFAULT_TEMPORARY_PASSWORD_EMAIL_PARAMS = {
        "subject": "Temporary password",
        "message": "Your temporary password is %s ",
        "from_email": settings.INVITES_DEFAULT_MAIL
    }
    return DEFAULT_TEMPORARY_PASSWORD_EMAIL_PARAMS


DEFAULT_OTP_SENT_EMAIL_PARAMS = {
    "subject": "OTP for login by invitee team.",
    "message": "Your OTP is ",
    "from_email": settings.INVITES_DEFAULT_MAIL
}
