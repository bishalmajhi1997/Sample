from django.shortcuts import render
from django.contrib import admin
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['city']
# Create your views here.
