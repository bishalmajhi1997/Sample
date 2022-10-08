"""user related forms"""
from django import forms
from django.contrib.auth.forms import (UserCreationForm as BaseUserCreationForm,
                                       UserChangeForm as BaseUserChangeForm)
from django.contrib.auth import get_user_model
from .models import SMSDevice
from .constants import DeviceType
from .services import normalize_email

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    """user creation form for the admin panel"""
    email = forms.EmailField(required=True)

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ("address_line_1", "address_line_2", "email", "state", "country", "city",
                  "department", "is_admin", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        if email:
            user.email = normalize_email(email)
        if commit:
            user.save()
        return user


class UserChangeForm(BaseUserChangeForm):
    """update form for admin panel"""
    email = forms.EmailField(required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        if email:
            user.email = normalize_email(email)
        if commit:
            user.save()
        return user


class SMSDeviceForm(forms.ModelForm):
    name = forms.ChoiceField(choices=DeviceType.choices())

    class Meta:
        model = SMSDevice
        fields = "__all__"
