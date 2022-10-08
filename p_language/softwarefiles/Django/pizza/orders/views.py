from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import OrderCreationSerailizer,OrderDetailSerailizer,OrderStatusUpdateSerializer
from .models import Order
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
# Create your views here.
User=get_user_model()
class HelloOrderView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Hello Orders")
    def get(self,request):
        return Response(data={"message":"Hello Order"},status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):
    serializer_class=OrderCreationSerailizer
    queryset=Order.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(operation_summary="List all orders made")
    def get(self,request):
        orders=Order.objects.all()
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(operation_summary="Create a new order")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        user=request.user
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    serializer_class=OrderDetailSerailizer
    permission_classes=[IsAdminUser]
    @swagger_auto_schema(operation_summary="Retrieve an order by id")
    def get(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(operation_summary="Update an order by id")
    def put(self,request,order_id):
        data=request.data
        order=get_object_or_404(Order,pk=order_id)
        #order=self.serializer_class(data=data,instance=order)
        serializer=self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_summary="remove/delete an order")
    def delete(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class=OrderStatusUpdateSerializer
    permission_classes=[IsAdminUser]
    @swagger_auto_schema(operation_summary="Update an orders status")
    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        data=request.data
        serializer=self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserOrdersView(generics.GenericAPIView):
    serializer_class=OrderDetailSerailizer
    @swagger_auto_schema(operation_summary="Get all orders for all users")
    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)
        orders=Order.objects.all().filter(customer=user)
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
class UserOrderDetail(generics.GenericAPIView):
    serializer_class=OrderDetailSerailizer
    @swagger_auto_schema(operation_summary="Get a users specific order")
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)
        orders=Order.objects.all().filter(customer=user).filter(pk=order_id)
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
