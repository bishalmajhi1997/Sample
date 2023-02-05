from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializers
from rest_framework.throttling import ScopedRateThrottle


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'



class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'


