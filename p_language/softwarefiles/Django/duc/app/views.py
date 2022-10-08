from django.shortcuts import render,redirect
from django.views.generic import View
from .form import *
# Create your views here.
def home(request):
    return render(request,'core/home.html')
class Signupview(View):

    def get(self,request):
        fm=SignUpForm()
        return render(request,'core/signup.html',{'form':fm})
    def post(self,request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():

             fm.save()
             return redirect('/home')
        else:
             return render(request,'core/signup.html',{'form':fm})
