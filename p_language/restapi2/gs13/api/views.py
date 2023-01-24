from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from .models import Student
from .serializers import StudentSerializers

class StudentListAPIView(ListModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreateAPIView(CreateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrieveAPIView(RetrieveModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class StudentUpdateAPIView(UpdateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDeleteAPIView(DestroyModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

