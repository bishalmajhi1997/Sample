from django.shortcuts import render
from django.contrib import admin
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[OrderingFilter]
    # ordering_fields=['city','name']
    # ordering_fields=['city']
    ordering_fields='__all__'
    

# Create your views here.
