from django.db import models
#abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)
# Create your models here.
"""user related models"""
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager, AnonymousUser as BaseAnonymousUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django_otp.models import SideChannelDevice, ThrottlingMixin
from phonenumber_field.modelfields import PhoneNumberField
from utils.abstract_models import AbstractDateTimeModel


class UserManager(BaseUserManager):
    """extended user manager"""

    # pylilnt
    def _create_user(self,phone, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone:
            raise ValueError('The given phone must be set')
        if extra_fields.get("email"):
            extra_fields["email"] = self.normalize_email(extra_fields.get("email"))
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """create user"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """create super user"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    """User model"""

    #class DepartmentChoices(models.TextChoices):
        """
            department choice with this we care aggregate the user is form witch department
            for the host and invitees will be the Custom user
            for the employees' relation other will be used
        """

    #    CUSTOM_USER = "custom_user"
    #    SALES = "sales"
    #    FINANCE = "finance"
    #    SUPPORT = "support"

    DepartmentChoices=(
                ("CUSTOM_USER","custom_user"),
                ("SALES","sales"),
                ("FINANCE","finance"),
                ("SUPPORT","support")
    )
    username_validator = UnicodeUsernameValidator()
    # PhoneNumberFiled help us  to manage the number with company code and also help to verify them country wise
    phone = PhoneNumberField(unique=True, help_text="user phone/mobile number used to send OTP verification code")

    email = models.EmailField(null=True, blank=True)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(null=True, blank=True, help_text="optional address line")
    state = models.CharField(max_length=50, help_text="country state")
    country = models.CharField(max_length=50, help_text="country")
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user/image", null=True, blank=True)
#    department = models.CharField(default=DepartmentChoices.CUSTOM_USER, max_length=30, choices=DepartmentChoices.choices)
    department=models.CharField(max_length=30,choices=DepartmentChoices,default="CUSTOM_USER")
    is_admin = models.BooleanField(default=False, help_text="decide that user is their department admin or not")
    postcode = models.IntegerField(null=True, blank=True)
    username = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    # overridden manager
    objects = UserManager()

    def __str__(self):
        """representation"""
        return f"{self.phone} - {self.email}"

    @property
    def is_sales_team_person(self):
        """ check is person is form sales department """
        return self.department == User.DepartmentChoices.SALES

    @property
    def is_support_team_person(self):
        """ check is person is form sales department """
        return self.department == User.DepartmentChoices.SUPPORT

    @property
    def is_finance_team_person(self):
        """ check is person is form sales department """
        return self.department == User.DepartmentChoices.FINANCE

    @property
    def is_customer(self):
        """ check is person is form sales department """
        return self.department == User.DepartmentChoices.CUSTOM_USER

    def phone_display(self):
        return f"+{self.phone.country_code}-{self.phone.national_number}"

    def clean(self):
        """here verifying some common validation for django forms """
        if not self.email:
            raise ValidationError("Please provide the email.")
        qs = self.__class__.objects.filter(email=self.email)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError({"email": "Email already exists."})


class SMSDevice(ThrottlingMixin, SideChannelDevice):
    """
    A :class:`~django_otp.models.SideChannelDevice` that delivers a token via
    the SMS service.
    The tokens are valid for :setting:`OTP_SMS_TOKEN_VALIDITY` seconds. Once
    a token has been accepted, it is no longer valid.
    .. attribute:: number
        *CharField*: The mobile phone number to deliver to.     """

    class Meta(SideChannelDevice.Meta):
        verbose_name = "SMS Device"

    def get_throttle_factor(self):
        return settings.OTP_SMS_THROTTLE_FACTOR

    def generate_challenge(self):
        """
        Sends the current TOTP token to ``self.number``.
        :returns: `CHALLENGE_MESSAGE` on success.
        :raises: Exception if delivery fails.
        """
        self.generate_token(valid_secs=settings.OTP_SMS_TOKEN_VALIDITY)

        message = settings.OTP_TOKEN_TEMPLATE.format(token=self.token)

        return message

    def verify_token(self, token):

        verify_allowed, message = self.verify_is_allowed()
        if verify_allowed:
            verified = super().verify_token(str(token))

            if verified:
                self.throttle_reset()
            else:
                self.throttle_increment()
        else:
            verified = False

        return verified, message


class BankDetail(AbstractDateTimeModel):
    """bank detail model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bank_detail")
    name = models.CharField(max_length=150, help_text="bank name", verbose_name="Bank name")
    bank_code = models.CharField(max_length=150, help_text="bank code", null=True, blank=True)
    number = models.CharField(max_length=150, help_text="bank account number", verbose_name="Account number")
    holder_name = models.CharField(max_length=150, help_text="bank account holder name", verbose_name="Holder name")

    def __str__(self):
        return f"{self.user.email}-{self.name}"


class Card(AbstractDateTimeModel):
    """saved debit or credit cards"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_cards")
    name_on_card = models.CharField(max_length=50)
    expired_time = models.CharField(verbose_name="DD/MM expired time", help_text="expired time on card", max_length=10)
    number = models.CharField(verbose_name="Card number", help_text="card number form debit/credit card", max_length=20)

    class Meta:
        unique_together = [['number', 'user']]

    def clean(self):
        """manage the django form validation on admin side"""
        if not self.pk:
            self._ensure_maximum_cards()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """extended cad save to customize validation"""
        if not self.pk:
            self._ensure_maximum_cards()
        super().save(force_insert, force_update, using, update_fields)

    def _ensure_maximum_cards(self):
        """ensure maximum card per user"""
        existing_card_count = self.__class__.objects.filter(user=self.user).count()
        if existing_card_count >= settings.MAX_NUMBER_OF_CARD_PER_USER:
            raise ValidationError("User reached max card limits.")


class AnonymousUser(BaseAnonymousUser):
    """override to update some methods"""

    @property
    def is_sales_team_person(self):
        """ check is person is form sales department """
        return False

    @property
    def is_support_team_person(self):
        """ check is person is form sales department """
        return False

    @property
    def is_finance_team_person(self):
        """ check is person is form sales department """
        return False

    @property
    def is_customer(self):
        """ check is person is form sales department """
        return False
