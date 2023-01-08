from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({"msg":"data created. "})


# @api_view(["GET"])
# def hello_world(request):
#     return Response({"msg":"data created. "})

# @api_view(["POST"])
# def hello_world(request):
#     print(request.data)
#     return Response({"msg":"This is post requested."})

@api_view(["GET","POST"])
def hello_world(request):
    if request.method=="GET":
         print(request.data)
         return Response({"msg":"This is GET requested."})
    if request.method=="POST":
         print(request.data)
         return Response({"msg":"This is GET requested.","data":request.data})
