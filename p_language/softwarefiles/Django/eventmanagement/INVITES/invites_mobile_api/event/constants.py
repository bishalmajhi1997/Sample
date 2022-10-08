"""declare event related constant here"""
from django.db.models import TextChoices


class EventCancellationChoices(TextChoices):
    """"event cancellation choices for event description"""
    PAYMENT_CONCERN = "payment_concern"
    DUPLICATE_REQUEST = "duplicate_request"
    FRAUD_REQUEST = "fraud_request"
    JUST_ENQUIRY = "just_enquiry"


EVENT_ATTEND_SUCCESS_MESSAGE = "Event is successfully attend by %s"
EVENT_CANCELLATION_MESSAGE = "Event is cancelled by %s"
EVENT_CREATE_SUCCESS_MESSAGE = "Event is successfully created by %s"
EVENT_UPDATE_SUCCESS_MESSAGE = "Event is successfully updated by %s"

WEEKLY_EVENT_NOTIFICATION_MESSAGE = "You have to attend the %s event in upcoming 7 days"
THREE_DAY_EVENT_NOTIFICATION_MESSAGE = "You have to attend the %s event at %s date."
