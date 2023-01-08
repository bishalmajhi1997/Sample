from django.contrib.auth.models import User
from .models import StudentInformation
from django import forms
class StudentInfoForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password',"email")

class StudentProfileInformationForm(forms.ModelForm):
    class Meta():
        model=StudentInformation
        fields="__all__"
 