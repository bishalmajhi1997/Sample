from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializers
from rest_framework import generics,mixins,authentication,permissions
# from django.http import get_object_or_404
from django.shortcuts import get_object_or_404

# using function based create retrieve or list
@api_view(["GET","POST"])
def product_alt_view(request,pk,*args,**kwargs):
    method=request.method#put,update,destroy,delete
    if method=="GET":
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializers(obj,many=False).data
            return Response(data)
        queryset=Product.objects.all()
        data=ProductSerializers(obj,many=True).data
        return Response(data)
        # urg_args?
        # get_request->details view
        # list view
    if method=="POST":
        # create an item
            serializer=ProductSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                    print(serializer.data)
                    title=serializer.validated_data.get("title")
                    content=serializer.validated_data.get("content")
                    if content is None:
                        content=title
                    serializer.save(content=content)
                   # data=serializer.data
                    return Response(serializer.data)
            return Response({"invalid":"Not good data"},status=400)










# generics
# mixins and genericsapiview
class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field="pk"
    def get(self, request,*args,**kwargs):
        print(args,kwargs)
        pk=kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def perform_create(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        if content is None:
            content="This is a single view doing cool stuff."
        serializer.save(content=content)
# genericdeleteapiview
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field="pk"
    def perform_destroy(self,instance):
        super().perform_destroy(instance)
 

# genericupadateapiview
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    lookup_field="pk"
    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title


# genericesCreateApiview
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    authentication=[authentication.SessionAuthentication]
    # permissions_classes=[permissions.IsAuthenticatedOrReadOnly]
    permissions_classes=[permissions.DjangoModelPermissions]
    def perform_create(self,serializer):
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        
        if content is None:
            content=title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

# post
class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    def perform_create(self,serializer):
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        
        if content is None:
            content=title
        serializer.save(content=content)

# get
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    # lookup_field="pk"
# product_detail_view=ProductDetailAPIView
class ProductListAPIView(generics.RetrieveAPIView):
    '''Not gona used this method'''
    queryset=Product.objects.all()
    serializer_class=ProductSerializers


# @api_view(["POST"])
# def api_home(request,*args,**kwargs):
#     serializer=ProductSerializers(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         print(serializer.data)
#         # data=serializer.data
#         return Response(serializer.data)
#     return Response({"invalid":"Not good data"},status=400)

# Create your views here.
# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
#     instance=Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         # data['id']=model_data.id
#         # data["title"]=model_data.title
#         # data["content"]=model_data.content
#         # data["price"]=model_data.price
#         # data=model_to_dict(model_data,fields=["id","title","price","sale_price"])
#         # return JsonResponse(data)
#         data=ProductSerializers(instance).data
#     return Response(data)

#         # # json_data_str=json.dumps(data)
#         # print(data)
#         # data=dict(data)
#         # json_data_str=json.dumps(data)

#         # model instance(model_data)
#         # turn a python dict
#         # return a json to my_client
#     # return JsonResponse(data)
#     # return HttpResponse(data,headers={"content_type":"application/json"})
#         # return HttpResponse(json_data_str,headers={"content_type":"application/json"})


