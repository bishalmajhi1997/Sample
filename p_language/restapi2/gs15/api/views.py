from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializers


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
