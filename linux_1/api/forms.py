from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.utils.translation import gettext_lazy as _

class StudentDetailsForm(forms.ModelForm):
    class Meta():
        model=Student
        fields={'first_name','last_name','email','phone'}
        widgets={'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'phone':forms.TextInput(attrs={'class':'form-control'}),
                }

class StudentRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta():
        model=User
        fields={'username','email','password1','password2'}
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_('email'),max_length=200,widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'email'}))
class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_('confirm new password'),max_length=200,strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}))
    new_password2=forms.CharField(label=_('confirm new password'),max_length=200,strip=False,widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'new-password'}))
class MySetPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('old password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password','autofocus':True}))
    new_password1=forms.CharField(label=_('new password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password','autofocus':True}))
    new_password1=forms.CharField(label=_('confirm new password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password','autofocus':True}))