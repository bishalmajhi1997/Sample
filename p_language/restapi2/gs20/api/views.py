from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
class StudentModelViewSet(viewsets.ModelViewSet):
    # local authentication
    authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    permission_classes=[IsAdminUser]
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
