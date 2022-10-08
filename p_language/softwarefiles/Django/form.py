from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Password Again",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)

    class Meta:
        model=User
        fields=('username','email','first_name','last_name')
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
