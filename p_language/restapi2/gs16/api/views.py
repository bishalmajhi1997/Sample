from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializers


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
