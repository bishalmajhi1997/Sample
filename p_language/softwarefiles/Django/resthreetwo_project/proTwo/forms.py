from django import forms
from proTwo.models import User

class NewUser(forms.ModelForm):
    class Meta():
        model=User
        fields="__all__"
