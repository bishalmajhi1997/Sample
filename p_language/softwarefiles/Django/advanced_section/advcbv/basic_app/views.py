from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy

# Create your views here.
#CLASS BASED VIEWS
class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL !")
#FUNCTIONS BASED VIEWS
def help(request):
    return render(request,"index.html")
#CLASS BASED TEMPLATE VIEWS
class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["injectime"]="BASIC INJECTIONS !"
        return context
#CLASS BASED LIST VIEWS
class SchoolListView(ListView):
    context_object_name="schools"
    model=models.School
    template_name="basic_app/school_list.html"

#CLASS BASED DETAILS VIEWS
class SchoolDetailView(DetailView):
    context_object_name="school_detail"
    model=models.School
    template_name="basic_app/school_detail.html"
#CLASS BASED CREATE VIEWS
class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School
#CLASS BASED UPDATE VIEWS
class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School
#CLASS BASED DELETEVIEWS
class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy("list")
