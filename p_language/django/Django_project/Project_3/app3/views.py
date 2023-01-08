from django.shortcuts import render,redirect
from .forms import UserInfoForm,UserProfileInformation
# from django.contrib.auth import User
from django.urls import reverse
from .models import UserProfile
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,"app3/index.html")

def register(request):
    registered=False
    if request.method=="POST":
        # registered=False
        user_form=UserInfoForm(data=request.POST)
        profile_form=UserProfileInformation(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES["profile_pic"]
                profile.save()
                registered=True
    else:
        user_form=UserInfoForm()
        profile_form=UserProfileInformation()
        #dict5={"user_form":user_form,"profile_form":profile_form,"registered":registered}
        #print(dict5)
        #dict5={"user_form":user_form,"profile_form":profile_form,"registered":registered}
        #dict5={"user_form":user_form,"profile_form":profile_form,"registered":registered}
    return render(request,"app3/registrations.html",{"user_form":user_form,"profile_form":profile_form,"registered":registered})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
    #     if user:
    #         if user.is_active:
    #             login(request,user)
    #             return HttpResponseRedirect(reverse('index'))
    #         else:
    #             return HttpResponse("ACCOUNT NOT ACTIVE")
    #     else:
    #         print("Someone tried to login and Failed")
    #         print("Username:{} and password {}".format(username,password))
    #         return HttpResponse("Invalid login details supplied !")
    # else:
    #     return render(request,"app3/login.html")

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"username and password does not matches")
    context={}
    return render(request,"app3/login.html",context)

def user_logout(request):
    logout(request)
    return redirect('login')
