# This wrapper provide a few bits of functionality such as making sure you receive request instance in your view and adding context 
# to response objects so that content negotitaioncan be performed.
# Thw wrapper also provide behaviou such as returning 405 method not allowed repsponses when appropriate and handling any parseError exceptions
# that occur when accessing request.data with malformed.
# By default only get method will be accepted .other methods will respond 405 method not allowed.
# @api_view()
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def function_name(request):
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# @api_view(["GET"])
# def student_list(request):
#     if request.method=='GET':
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# @api_view(["POST"])
# def student_list(request):
#     if request.method=='POST':
#         serializer=StudentSerializer(Data=request.data)
#         if serializer.is_valid():
            #   serializer.save()
            # res={"msg":"data created"}
            #   return Response(res,status=status.HTTP_201_CREATED)
        # return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

# GET,POST,PUT,PATCH,DELETE-METHODS
# RESPONSE(data,status=None,template_name=None,headers=None,content_type=None)

