from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


class StudentModelViewSet(viewsets.ModelViewSet):
    # local authentication
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
