from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("*******list*********")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Descriptions:",self.description)

        stu=Student.objects.all()
        serializer_class=StudentSerializers(stu,many=True)
        return Response(serializer_class.data)
    
    def retrieve(self,request,pk=None):
        print("*******retrieve*********")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Descriptions:",self.description)

        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer_class=StudentSerializers(stu)
            return Response(serializer_class.data)
    
    def create(self,request):
        print("*******create*********")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Descriptions:",self.description)

        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data created."},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        print("*******update*********")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Descriptions:",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        print("*******partial_update*********")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Descriptions:",self.description)

        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Partial Data updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        print("*******delete*********")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Descriptions:",self.description)

        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted."},status=status.HTTP_200_OK)

