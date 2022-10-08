from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.utils.translation import ugettext_lazy as _,ugettext_lazy
from django.core.validators import validate_email
#from verified_email_field.forms import VerifiedEmailField
from email_validator import validate_email
class UserRegisterForm(UserCreationForm):
    #email=validate_email('example@example.com')
    email=forms.EmailField()
        #email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    #phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    #password=forms.CharField(widget=forms.PasswordInput())
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Password Again",widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = [ "username",'email','first_name','last_name']
    #def clean_email(self):
    #    email=forms.EmailField()
    #    email_passed=self.cleaned_data.get("email")
    #    email_req="bishalmajhi1997@gmail.com"
    #    if not email_req in email_passed:
    #        raise forms.ValidationError("invalid email Format")
    #    return email_passed
    #    email=validate_email(email_passed)
    #   if email:

    #        raise forms.ValidationError("invalid email Format")
    #    return email
