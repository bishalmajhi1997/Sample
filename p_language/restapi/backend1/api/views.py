from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
def index(request,*args,**kwargs):
    # request-httprequest-django
    # print(dir(request))
    # print(request.body)
    print(request.GET)#QUERY PARAMS
    print(request.POST)
    body=request.body#byte string of json data
    data={}
    print(body)
    try:
        data=json.loads(body)#string of json data to python dict
    except:
        pass
    print(data)
    # data["headers"]=request.headers#request.META
    print(request.headers)
    data["params"]=dict(request.GET)
    data["headers"]=dict(request.headers)
    data["content_type"]=request.content_type
    return JsonResponse(data)