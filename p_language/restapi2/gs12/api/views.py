from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPIView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializers=StudentSerializers(stu)
            return Response(serializers.data)
        stu=Student.objects.all()
        serializers=StudentSerializers(stu,many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg":"Data_created"})
        return Response(serializers.errors)
    
    def put(self,request,pk=None,format=None):
        ID=pk
        stu=Student.objects.get(pk=ID)
        serializers=StudentSerializers(stu,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':"Data_updated"},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        ID=pk
        stu=Student.objects.get(pk=ID)
        serializers=StudentSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':"Partial_Data_updated"},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data_deleted."})






