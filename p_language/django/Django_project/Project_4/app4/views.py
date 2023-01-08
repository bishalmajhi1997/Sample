from django.shortcuts import render,redirect
from app4 import forms
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"app4/index.html")
def regsitrations(request):
    registered=False
    if request.method=="POST":
        stu_info_form=forms.StudentInfoForm(request.POST)
        stu_profile_info=forms.StudentProfileInformationForm(request.POST)
        if stu_info_form.is_valid() and stu_profile_info.is_valid():
            stu=stu_info_form.save()
            stu.set_password(stu.password)
            stu.save()
            stu_profile_info.save(commit=False)
            registered=True
    else:
        stu_info_form=forms.StudentInfoForm()
        stu_profile_info=forms.StudentProfileInformationForm()
    return render(request,"app4/registrations.html",{"stu_info_form":stu_info_form,"stu_profile_info":stu_profile_info,"registered":registered})
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"username and password does not matches")
    context={}
    return render(request,"app4/login.html",context)

def user_logout(request):
    logout(request)
    return redirect('login')



