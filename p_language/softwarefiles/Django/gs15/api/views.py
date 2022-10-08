from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
#from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from api.custompermissions import MyPermission
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
#from .custompermissions import MyPermission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
# no1 BasicAuthentication  authentication_classes=[BasicAuthentication]
#no1.    #permission_classes=[IsAuthenticated]#permission_classes=[AllowAny]#permission_classes=[IsAdminUser]
#No.2SessionAuthentication
#    authentication_classes=[SessionAuthentication]
# no2   permission_classes=[IsAuthenticated]#permission_classes=[AllowAny]#permission_classes=[IsAdminUser]#permission_classes=[IsAuthenticatedOrReadOnly]#permission_classes=[DjangoModelPermissions]#permission_classes=[DjangoModelPermissionsOrAnonReadOnly]#
#no3 Mypermissions
    authentication_classes=[SessionAuthentication]
    permission_classes=[MyPermission]
