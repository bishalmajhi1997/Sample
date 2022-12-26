from django.shortcuts import render
from .models import User
from app2 import forms
from django.http import HttpResponse
# Create your views here.
def User1(request):
    dict1=User.objects.order_by("email")
    context={"dict1":dict1}
    return render(request,"app2/user2.html",context=context)
def FormNameView(request):
    form=forms.FormName()
    if request.method=="POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("validation success")
            print("first name: "+form.cleaned_data["first_name"])
            print("Last name: "+form.cleaned_data["last_name"])
            print("Email: "+form.cleaned_data["email"])
    context={"forms":form}
    return render(request,"app2/forms.html",context=context)
def index(request):
    return render(request,"app2/index.html")
def FormNameView2(request):
    form=forms.NewUserForm()
    if request.method=="POST":
        form=forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error:Form is Invalid")
    context={"forms2":form}
    return render(request,"app2/forms2.html",context=context)


def Student_Form(request):
    form=forms.Student_Form()
    if request.method=="POST":
        form=forms.Student_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Full Name:"+form.cleaned_data["name"])
            print("Age:"+str(form.cleaned_data["age"]))
            print("Contact:"+str(form.cleaned_data[str("contact")]))
            print("Address:"+form.cleaned_data["address"])
            print("validation Success")
            return HttpResponse("Validation Success")
    context={"forms3":form}
    return render(request,"app2/form3.html",context=context)
