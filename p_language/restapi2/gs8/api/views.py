from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id",None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")
    
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,"application/json")
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id")
        student=Student.objects.get(id=id)
        # complete updated
        # serializer=StudentSerializers(student,data=pythondata)
        # partial updated
        serializer=StudentSerializers(student,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data Updated"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,"application/json")

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id")
        student=Student.objects.get(id=id)
        student.delete()
        res={"msg":"Data deleted"}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,"application/json")














# @csrf_exempt
# def StudentGET(request):
#     if request.method=="GET":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get("id",None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializers(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type="application/json")
#         stu=Student.objects.all()
#         serializer=StudentSerializers(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type="application/json")
    
#     if request.method=="POST":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializers(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data created"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type="application/json")
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,"application/json")

#     if request.method=="PUT":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get("id")
#         student=Student.objects.get(id=id)
#         # complete updated
#         # serializer=StudentSerializers(student,data=pythondata)
#         # partial updated
#         serializer=StudentSerializers(student,data=pythondata,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res={"msg":"Data Updated"}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type="application/json")
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,"application/json")

#     if request.method=="DELETE":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get("id")
#         student=Student.objects.get(id=id)
#         student.delete()
#         res={"msg":"Data deleted"}
#         json_data=JSONRenderer().render(res)
#         return HttpResponse(json_data,"application/json")


