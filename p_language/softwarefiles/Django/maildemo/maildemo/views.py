from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail

def home(request):
    return render(request,"home.html")

def send_gmail(request):
    if request.method=="POST":
        name=request.POST.get("name")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        print(name,subject,message)
        send_mail(subject,message,"bishalmajhi1997@gmail.com",['bishal_19mc008@gita.edu.in'],fail_silently=False)
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse("invalid request")
