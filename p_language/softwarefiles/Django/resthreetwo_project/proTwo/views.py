from django.shortcuts import render
from proTwo.forms import NewUser

# Create your views here.
def index(request):
    return render(request,"protwo/index.html")

def users(request):
    form=NewUser()
    if request.method=="POST":
        form=NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error form invalid")
    return render(request,'protwo/users.html',{"form":form})
