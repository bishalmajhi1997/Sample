from django import forms
from .models import User,Student
# from address.forms import AddressField

class FormName(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=30)
class NewUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = "__all__"
class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
