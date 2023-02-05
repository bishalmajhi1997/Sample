from django.shortcuts import render
from django.contrib import admin
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView


class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    

# Create your views here.
