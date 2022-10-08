from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives


from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

def home(request):
    return render(request,'basic_app/index.html')

def send_gmail(request):
    registered=False
    if request.method=="POST":

        NAME=request.POST.get('name')
        SUBJECT=request.POST.get('subject')
        message=request.POST.get('message')
        password=request.POST.get('password')
        userid=request.POST.get('email')

        print(NAME,SUBJECT,message,password)
        send_mail(SUBJECT,
              message,
              'bishalmajhi1997@gmail.com',
              ['bishal_19mc008@gita.edu.in'],
              fail_silently=False,)


            #subject, from_email, to = 'su', 'bishalmajhi1997@gmail.com', 'bishal_19mc008@gita.edu.in'
            #text_content = 'This is an important message.'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
        #msg = EmailMultiAlternatives(SUBJECT, message,'bishalmajhi1997@gmail.com', ['bishal_19mc008@gita.edu.in'])
        #msg.attach_alternative(message,SUBJECT)
        #msg.send()

        registered=True
    else:
       print("invalid email")
    return render(request,'basic_app/index.html',{'registered':registered})
