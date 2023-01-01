from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class UserInfoForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password',"email")

class UserProfileInformation(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=('portfolio_site','profile_pic')