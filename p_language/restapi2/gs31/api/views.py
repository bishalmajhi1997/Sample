from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import My_Permission
from .customauth import CustomAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from .throttling import JackRateThrottle
class StudentModelViewSet(viewsets.ModelViewSet):
    # local authentication
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=[IsAdminUser]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[My_Permission]
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    # throttle_classes=[UserRateThrottle,AnonRateThrottle]
    throttle_classes=[JackRateThrottle,AnonRateThrottle]

