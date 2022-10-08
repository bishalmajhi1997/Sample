from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import UserCreationSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Hello auth")
    def get(self,request):
        return Response(data={"message":"Hello Auth"},status=status.HTTP_200_OK)

class UserCreateView(generics.GenericAPIView):
    serializer_class=UserCreationSerializer
    @swagger_auto_schema(operation_summary="Create a user account.")
    def post(self,request):
        data=request.data
        serailizer=self.serializer_class(data=data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(data=serailizer.data,status=status.HTTP_201_CREATED)
        return Response(data=serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
