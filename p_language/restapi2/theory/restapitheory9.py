# CONCRETE VIEW CLASS
# The following classes are the concrete generic views.
# if you are using generic views this is normally the level you will be working at unless you need heavily customized behaviour.
# LISTAPIVIEW,CREATEAPIVIEW,RETRIEVEAPIVIEW,UPDATEAPIVIEW,DESTROYAPIVIEW,LISTCREATEAPIVIEW,RETRIEVEUPDATEAPIVIEW,RETRIEVEDESTROYAPIVIEW,RETRIEVEDESTROYUPDATEAPIVIEW

# LISTAPIVIEW
# It is used for read-only endpoints to represent a collection of model instance.it provides a get method handler.
# Extends-GenericAPIView,ListModelMixin
# from rest_framework.generics import ListAPIView
# class StudentList(ListAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# CREATEPIVIEW
# It is used for create-only endpoints.it provides a post method handler.
# Extends-GenericAPIView,CreateModelMixin
# from rest_framework.generics import CreateAPIView
# class StudentList(CreateAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# RETRIEVEAPIVIEW
# It is used for create-only endpoints to repesent a single model instance.it provides a get method handler.
# Extends-GenericAPIView,RetrieveModelMixin
# from rest_framework.generics import RetrieveAPIView
# class StudentList(RetrieveAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# UPDATEAPIVIEW
# It is used for update-only endpoints to repesent a single model instance.it provides a put and patch method handler.
# Extends-GenericAPIView,UpdateModelMixin
# from rest_framework.generics import UpdateAPIView
# class StudentList(UpdateAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer
    
# DestroyAPIVIEW
# It is used for delete-only endpoints to repesent a single model instance.it provides delete method handler.
# Extends-GenericAPIView,DestroyModelMixin
# from rest_framework.generics import DestroyAPIView
# class StudentList(DestroyAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# ListCreateAPIView
# It is used for read-write-only endpoints to repesent a collection of model instance.it provides get and post method handler.
# Extends-GenericAPIView,ListModelMixin,CreateModelMixin
# from rest_framework.generics import ListCreateAPIView
# class StudentList(ListCreateAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# RetrieveUpdateAPIView
# It is used for read or update endpoints to repesent a single model instance.it provides get,put and patch  method handler.
# Extends-GenericAPIView,RetrieveModelMixin,UpdateModelMixin
# from rest_framework.generics import RetrieveUpdateAPIView
# class StudentList(RetrieveUpdateAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer
# RetrieveUpdateAPIView
# It is used for read or update endpoints to repesent a single model instance.it provides get,put and patch  method handler.
# Extends-GenericAPIView,RetrieveModelMixin,UpdateModelMixin
# from rest_framework.generics import RetrieveUpdateAPIView
# class StudentList(RetrieveUpdateAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# RetrieveDestroyAPIView
# It is used for read or delete endpoints to repesent a single model instance.it provides get and delete method handler.
# Extends-GenericAPIView,RetrieveModelMixin,DestroyModelMixin
# from rest_framework.generics import RetrieveDestroyAPIView
# class StudentList(RetrieveDestroyAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# RetrieveUpdateDestroyAPIView
# It is used for read or write or delete endpoints to repesent a single model instance.it provides get,put,patch and delete method handler.
# Extends-GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# class StudentList(RetrieveUpdateDestroyAPIView):
        # queryset=Student.objects.all()
        # serializer_class=StudentSerializer

# 