from django.shortcuts import render
from django.contrib import admin
from .models import Student
from .serializers import StudentSerializers
from .mypaginations import MypageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
#     pagination_class=MypageNumberPagination

class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    # pagination_class=PageNumberPagination   
    pagination_class=MypageNumberPagination  

# Create your views here.
