from django.shortcuts import render,HttpResponse
from .models import AccessRecord,WebPage
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"app1/index.html")
def Home(request):
    return render(request,"app1/home.html")
def cotact(request):
    dict1={"name":"john","age":28}
    return render(request,"app1/contact.html",context=dict1)
def Webpage(request):
    webpage_list=AccessRecord.objects.order_by("date")
    dict1={"access_record":webpage_list}
    return render(request,"app1/webpagelist.html",context=dict1)
def webpage1(request):
    webpage_list1=WebPage.objects.all()
    dict2={"webpage_list":webpage_list1}
    return render(request,"app1/webpage1.html",context=dict2)
