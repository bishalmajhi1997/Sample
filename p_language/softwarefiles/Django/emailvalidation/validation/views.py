from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from basic_app.forms import UserForm
from basic_app.forms import UserProfileInfoForm

# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.site.shortcuts import get_current_site
def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()

            current_site=get_current_site(request)
            mail_subject
