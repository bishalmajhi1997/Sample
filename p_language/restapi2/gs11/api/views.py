from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
# Create your views here.
@api_view(["GET","POST","PUT","PATCH","DELETE"])
def StudentView(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializers=StudentSerializers(stu)
            return Response(serializers.data)
        stu=Student.objects.all()
        serializers=StudentSerializers(stu,many=True)
        return Response(serializers.data)
    if request.method=="POST":
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg":"Data_created"})
        return Response(serializers.errors)
    if request.method=="PUT":
        ID=pk
        stu=Student.objects.get(pk=ID)
        serializers=StudentSerializers(stu,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':"Data_updated"},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="PATCH":
        ID=pk
        stu=Student.objects.get(pk=ID)
        serializers=StudentSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':"Partial_Data_updated"},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data_deleted."})