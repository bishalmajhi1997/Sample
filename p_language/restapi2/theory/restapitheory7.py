# RESTFRAMEWORK provides an apiview class,,which subclass djangos view class.
# APIVIEW classes are different from regular view classes in the following ways
# request passed to the handlers methods will be rest framework request instances,not djangos httprequest instace.
# Handlers methods may return rest framework response,instead of django httpresponse.the view will manage content negotitaion and setting the correct render on the response.
# Any api exceptions exceptions will be caught and mediated into appropriate response. 
# Incoming requests will be authenticated and appropriate permissions and/or throttle checks will be run before dispatching the request to the handler method.
# syntax:
# from rest_framework.views import APIView
# class Student(APIView):
#     def get(self,request,format=None):
#         stu=Student.objects.all() 
#         serialzer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     def post(self,request,format):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"mgs":"Dtaa_created"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status,HTTP_400_BAD_REQUEST)