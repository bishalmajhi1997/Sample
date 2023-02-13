from django.shortcuts import render

# Create your views here.
from django. shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import messages
# from .forms import StudentDetailsForm,StudentRegistrationForm
from .models import Student,Profile
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .forms import StudentDetailsForm,StudentRegistrationForm
from django.views import View
# Create your views here
def index(request):
    return render (request,'api/index.html')
def team(request):
    return render (request,'api/team.html')
def contact(request):
    return render (request,'api/Contact.html')
def innerpage(request):
    return render (request,'api/innerpage.html')
def login1(request):
    return render (request,'api/login1.html')
def signup(request):
    return render (request,'api/signup.html')                    

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username=username).first():
                messages.success(request,"Username is taken")
                return redirect('/register')
            user_obj=User(username=username,email=email)
            user_obj.set_password('password')
            user_obj.save()
            auth_token=str(uuid.uuid4())
            profile_obj=Profile.objects.create(user=user_obj,auth_token=auth_token)
            profile_obj.save()
            send_email_after_registration(email,auth_token)
            return redirect('/token')
        except Exception as e:
            print(e)
    return render(request,'api/register.html')
def send_email_after_registration(email,token):
    subject="This account need to be verified."
    messages=f'hi paste the link the verify your account http://127.0.0.1:8000/verify/{token}'
    email_form=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,messages,email_form,recipient_list)
def verify(request,auth_token):
    try:
        profile_obj=Profile.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request,"Your account is already verified.")
                return redirect('/accounts/login')
            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request,"your account has been verified.")
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        
        login(request , user)
        return redirect('/details')

    return render(request , 'api/login1.html')
# def user_login(request):
#     if request.method =="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user_obj=User.objects.filter(username=username).first()
#         if user_obj is not None:
#             messages.success(request,'user not found.')
#             return redirect('/accounts/login')
#         profile_obj=Profile.objects.filter(user=user_obj).first()
#         if profile_obj is not None:
#             messages.success(request,"profile is not verified check your mail")
#             return redirect('/accounts/login') 
#         user=authenticate(username=username,password=password)
#         if user is None:
#             messages.success(request,'wrong password')
#             return redirect('/accounts/login')
#         login(request,user)
#         return redirect('api:details')  
#     return render(request,'api/login1.html')

def user_logout(request):
    logout(request)
    return redirect('/accounts/login') 

class DetailView(View):
    def get(self,request):
        form=StudentDetailsForm()
        return render(request,'api/details.html',{'form':form})
    def post(self,request):
        form=StudentDetailsForm(request.POST)
        if form.is_valid():
            usr=request.user
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            reg=Student(user=usr,first_name=first_name,last_name=last_name,email=email,phone=phone)
            reg.save()
            messages.success(request,'Congratulations ! Profile updated Successfully')
            return redirect('/innerpage')
        return render(request,'api/details.html',{'form':form,'active':'btn-primary'})


def error_page(request):
    return render(request,'api/error.html')
def success(request):
    return render(request,'api/success.html')
def token_send(request):
    return render(request,'api/success.html')

