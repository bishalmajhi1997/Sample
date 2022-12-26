# DJANGO REST FRAMEWORK
# Django rest framework is a powerful and flexible toolkit for buildibg web api.
# Authentication policies including packages for oauth1 and oauth2.
# Serialization that supports both orm and non-orm data sources.  
# Customize all the way down:Just use regular function-based views. if you don't need the more poweful features.
# Extensive documentation,and great community support.
# Used and trusted by internationally recognized companies including mozila,red hat,heroku and eventbrite.

# REQUIREMENTS
# Python,django
# The following packages are optional.
# PyYAML,uritemplate,markdown,pygments,django-filter,django-guardian
# pip freeze
# python --version
# django-admin --version
# pip install djangorestframework
# pip uninstall djangorestframework

# Python JSON
# python has a built in package called json,which is is used to work with json data.
# dumps(data):this is used to convert python object into json string.
# To use json packages first we have to imporve it.
# import json
# python data={"name":"bishal","roll":101}
# json_data=json.dumps(python data)
# print(json_data)
# {"name":"soname","roll":101}
# loads(data):This is used to json string.
# import json
# json_data={"name":"sonam","roll":101}
# parsed_data=json.loads(json_data)
# print(parsed_data)
# {"name":"Soname","roll":101}
# dumps:python to json string
# loads:json string ton python 

# Serialization and deserization
# In Django REST FRAMEWORK ,serializers are responsible for converting complex data
# such as querysets and model instances to native python datatypes(called serialization)
# that can then be easily rendered into JSON,XML or other content types which is easily understandable by Front End.

# Serializers are also responsible for desrilization which means it allows parsed data to be converted back 
# into complex types,after first validating the incoming data.
# serialization and deserialization

# Serializer Class
# A serializer class is very similar to a djangoform and model form class,and includes similar validation flags
# on the various fields,such as required field,max_length,and default.
# DRF provides  a serializer class which gives you a powerful,generic  way to control the output of your response,as well as modelclass
# which provides  a useful shortcut for creating serializers that deal with model instances and querysets.


# how to create serializer class
# create a separate serializers.py file to write all serializers.
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
# complex data type(serialization)=>pyhon native datatype(render into json)=>json data
# Creating query set
# stu=Student.objects.all()

# converting queryset to list of python dict/serializing query set.
#      serilaizer=StudentSerializer(stu,many=True)

# Serilizer data
# This is the serializer data.
# serializer.data

# JSONRenderer
# This is used to render Serialized data into JSON  which is understandable by front end.
# Importing JSONRenderer
# from rest_framework.renderers import JSONRenderer

# Render the data into JSON
# JSON_DATA=JSONRenderer().render(serializer.data)

# Complex datatype      Python native datatype     
# model object 1==>(Serilzation)==>Python dict==> (renderinto json)==>JsonData
# stu=Student.object.get(id=1)    serializer=StudentSerializer(stu)    json_data=JSONRenderer().render(serializer.data)

# JSONResponse
# JsonResponse(data,encoder=DjangoJSONEncoder,safe=True,json_dumps_params=None,**kwargs)
# An HttpResponse subclass that helps to create a JSON-encoded response.It inherits most behaviour from its superclass with a couple differences.
# 1.Its default content type-Type header is set to application/json.
# 2.The first parameter,data,should be  a dict instance.if the safe parameter is set to false it can be JSON-serializable object.
# 3.The encoder,which defaults to django.core.serilaizers.json.DjangoJSONEndcoder,will be used to serialize data.
# 4.The safe boolean parameters defaults to True.if its is not False,any object can be passed for serilization(otherwise only dict instance are allowed.)
# if safe is True and a non-dict object is passed  as the first argument,a typeerror will be raised.
# 5.the json_dumps_params parameter is a dictionary of keyword arguments to pass the json.dumps() call used to generate the response. 