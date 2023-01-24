# GENERICAPI VIEW
# Attributes:This class extends RESTFRAMEWORK APIVIEWS class,adding commonly required behaviour for standard list and details views.
# Attributes-query_set,serializer_class,lookup_field,lookup_url_kwarg,pagination_class,filter_backends
# Methods-get_queryset(self),get_object(self),get_serializer_class(self),get_selializer_context(self),get_paginated_response(self,data),paginate_queryset(self,queryset),filter_queryset(self,queryset)


# MIXINS
# One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behaviour.
# The create/retrieve/update/delete operations that we have been using so far are going to be pretty similar for any model-backend API-VIEWS we create.
# Those bits of common behaviour are implemented in REST_FRAMEWORK'S mixin classes.
# The mixin classes provide the actions that are used to provide the basic view behaviour.
# Note that the mixin classes provide action methods rather than defining the handler methods,such as get() and post(),directly.This allows for more flexible composition of behaviour.
# The mixins classes can be imported from rest_framework.mixins
# LISTMODELMIXINS
# CREATEMODELMIXINS
# RETRIEVEMODELMIXINS
# UPDATEMODELMIXINS
# DESTROYMODELMIXINS

# LISTMODELMIXINS:
# it provides a list(request,*args,**kwargs)method,that implements listing a queryset.if the queryset is populated,this returns 200 ok response,with a serialized representations of the queryset as the body of the response,The response data may be paginated.
# from rest_framework.mixins import ListModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentList(ListModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)


# CREATEMODELMIXINS:
# it provides a create(request,*args,**kwargs)method,that implements creating saving a new model instance.
# if an object is created this returns this returns a 201 created response,with a serialized represenation of the object as the body of the response.if the presentation contains a key named url,then the location header of the response will be populated with the value.
# if the request data provided for creating the object is invalid,a 400 bad request response will be returned,with the error details as the body of the response.
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentList(CreateModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# RETRIEVEMODELMODELMIXIN:
# it provide a retrieve(request,*args,**kwargs)method,that implements returning an existing model instance in a response.
# if an object can be retrieved this returns a 200 OK response,with a serialized represntation of the object as the body of the response.
# Otherwise it will return 404 Not Found.
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentList(RetrieveModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

# UPDATEMODELMIXIN:
# it provides a update(request,*args,**kwargs)method,which is similar to the updated method,except that all fields for the update will be optional.This allows support for HTTP PATCH requests.
# if an object is updated this returns a 200 OK response,with a serialized representation of the object as the body of the response.
# if the request data provided for updating the object was invalid,a 400 bad request response will be returned,with the error details as the body of the response.
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentList(UpdateModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

# DESTROYMODELMIXIN
# it provides a destroy(request,*args,**kwargs)method,that implements deletion of an existing model instance.
# if an object is deleted this returns a 204 no content response,otherwise it will return a 404 not found.
# from rest_framework.mixins import DestroyModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentList(DestroyModelMixin,GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



