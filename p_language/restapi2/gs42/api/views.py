from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    # local authentication
    # authentication_classes=[]
    # permission_classes=[My_Permission]
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
