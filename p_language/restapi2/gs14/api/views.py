from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from .models import Student
from .serializers import StudentSerializers
# list and post -pk is not required.
class StudentListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
# retrieve,update,delete-pk is required.
class StudentRetrieveUpdateDeleteAPIView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

