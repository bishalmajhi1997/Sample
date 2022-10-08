from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
#'''@api_view()
#def hello_world(request):
#    return Response({'msg':'Hello World'})
#@api_view(['GET'])
#def hello_world(request):
#    return Response({'msg':'Hello World'})
#@api_view(['POST'])
#def hello_world(request):
#    if request.method=='POST':
#        print(request.data)
#        return Response({'msg':'This is post request'})'''
@api_view(['GET','POST'])
def hello_world(request):
    if request.method=='GET':
        #print(request.data)
        return Response({'msg':'This is GET request'})

    if request.method=='POST':
        print(request.data)
        return Response({'msg':'This is post request','data':request.data})
