from django.shortcuts import render
from appthree.forms import NewUser
def index(request):
    return render(request,'appthree/index.html')
def users(request):
    form=NewUser()
    if request.method == "POST":

        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'appthree/user.html',{"form":form})

# Create your views here.
