from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"app1/index.html")
def Home(request):
    return render(request,"app1/home.html")
def cotact(request):
    dict1={"name":"john","age":28}
    return render(request,"app1/contact.html",context=dict1)