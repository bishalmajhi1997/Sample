#VIEWSET
#Django rest framework allows you to combine the logic for a set related views in a single class ,called VIEWSET.
# There are two main advantages of using a viewset over using a view class.
# Repeated logic can be combined into a single class.
# By using routers,we no longer need to deal with wiring up the url conf ourselves.
# A Viewset class is simply a type of class-based view,that does not provide any method handlers such as get() or post(),and 
# instead provides actions such as create() and list().
# list()-get all records.
# retrieve()-get single records.
# create()-create/insert completely.
# update()-update record completely.
# partial_update()-update record partially.
# destroy()-delete record
from rest_framework import viewsets
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):...
    def create(self,request):...
    def retrieve(self,request,pk=None):...
    def update(self,request,pk=None):...
    def partial_update(self,request,pk=None):...
    def destroy(self,request,pk=None):...
# During dispatch ,the following attributes are available on the ViewSet:-
# basename-the base to use for the url names that are created.
# action-the name of the current action(e.g.-list,create).
# detail-boolean indicating if the current action is configured for a list or detail view.
# suffix:the display suffix for the viewset type-mirrors the details attribute.
# name-the display name for the viewset.This argument is mutually exclusive to suffix.
# description-the display description for the individual view of a viewset.
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename="student")
urlpatterns=[
    path('',include(router.urls))
]


#MODELVIEWSET
# THE modelviewset class inherits from genericapiview and includes implementations for various actions,by mixing in the behaviour of the various mixin classes.
# The action provided by the modelviewset class are list(),retrieve(),create(),update(),partial_update() and destroy().you can use any of the standard attributes or method overrides provided by GenericAPIView.
# class StudentViewSet(viewsets.ModelViewSet):
#          queryset=Student.objects.all()
#          serializer_class=StudentSerializer



# READONLYMODELVIEWSET
# The readonlymodelviewset class also inherits from genericapiview.as with modelviewset it also includes implemenations for various actions,but unlike modelviewset only provides the 'read_only' actions,list() and retrieve().you can use any of the standard attributes and method overrides availables to genericapiview.
# class Studentreadonlymodelviewset(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


