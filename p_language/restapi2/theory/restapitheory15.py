# Filtering
# The simplest way to filter the queryset of any view that subclasses GenericAPIView is to override the .get_queryset() method.

# Generic Filtering
# Rest framework also includes support for generic filtering backends that allow you to easily construct complex searches and filters.

# DjangoFilterBackend
# The django-filter library includes  a DjangoFilterBackend class which supports highly customizable field filtering for rest framework.
# To use DjangoFilterBackend,first install django-filter.
# pip install django-filter
# Then add 'django-filters' to Django's INSTALLED_APPS:
#    ['django_filters']


# Global Settings
# settings.py
#  REST_FRAMEWORK={
#     'DEFAULT_FILTER_BACKENDS':
#      ['django_filters.rest_framework.DjangoFilterBackend']
#  }
 

# Local Settings
# Per view settings
# you can set the filter backends on a per-view, or per-viewset basis,using the GenericAPIView class-based views.
# from django_filters.rest_framework import DjangoFilterBackend
# class StudentListView(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers
#     filetrs_backend=[DjangoFilterBackend]


# DjnagoFilterBackend
# if you all need is simply equality-based filtering,you can set  a filterset_fields attribute on the view,or viewset,listing the set of fields you wish to filter against.
# from django_filters.rest_framework import DjangoFilterBackend
# class StudentListView(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers
#     filetrs_backend=[DjangoFilterBackend]
#     filterset_fields=['name','city']


# SearchFilter
# The searchfilter supports simple single query parameter based searching,and is based on the django admin's search functionality.
# The searchFilter class will be applied if the view has a search_fields attribute set.The search_fields attribute should be a list of names  of text types fields on the model,such as CharField() or TextField().
# class StudentListView(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers
#     filetrs_backend=[SearchFilter]
#     search_fields=['city']
# http://127.0.0:8000/studentapi/?search=Ranchi
# '^' starts-with search
# '=' exact matches
# '@' full text search (currently only supported django's postgresql)
# '$' regex search
# example 
# search_fields=['^name',]

# OrderingFilter
# The orderingfilter class supports simple query parameter controlled ordering of results.
# http://127.0.0.1:8000/studentapi/ordering=name
# The client may also specify reverse ordering by prefixing the field name with '-',like so:
# http://127.0.0.1:8000/studentapi/ordering=-name
# Multiple ordering may also be specified.
# http://example.com/api/users?ordering=account,username
# Its recommended that you explicitly specify which fields the api should allowing in the ordering filter.You can do this by setting an ordering_fields attribute on the view,like so:
# class StudentListView(generics.ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends=[OrderingFilter]
#     ordering_fields=['name']
#     ordering_fields=['name','city']
#     ordering_fields='__all__'


