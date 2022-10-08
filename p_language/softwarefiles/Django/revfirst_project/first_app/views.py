from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>My world</h1>")
def help(request):
    my_dict={"insert_me":"Hello i am from views.py"}
    return render(request,"first_app/index.html",context=my_dict)
def raja(request):
    my_dict={"eshwar":"I am Eswar"}
    return render(request,"first_app/index.html",context=my_dict)
def image(request):
    return render(request,"first_app/index.html")
