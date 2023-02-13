from django.shortcuts import render
from django.contrib import admin
from .models import Student
from .serializers import StudentSerializers
from .mypaginations import MyCursorPagination
from rest_framework.generics import ListAPIView
#     pagination_class=MypageNumberPagination

class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    pagination_class=MyCursorPagination

# Create your views here.
