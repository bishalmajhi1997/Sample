from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def StudentView(request,pk):
    student=Student.objects.get(id=pk)
    print(student)
    serilizer=StudentSerializers(student)
    print(serilizer)
    print(serilizer.data)
    # json_data=JSONRenderer( ).render(serilizer.data)
    # print(json_data)
    # data=json_data
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serilizer.data)
def StudentViewall(request):
    Student1=Student.objects.all()
    print(Student1)
    serilaizer=StudentSerializers(Student1,many=True)
    print(serilaizer)
    print(serilaizer.data)
    return JsonResponse(serilaizer.data,safe=False)