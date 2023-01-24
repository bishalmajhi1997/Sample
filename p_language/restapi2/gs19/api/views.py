from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
