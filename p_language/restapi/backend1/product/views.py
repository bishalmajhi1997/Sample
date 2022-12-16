from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from product.models import Product
from django.forms.models import model_to_dict
# Create your views here.
def api_home(request,*args,**kwargs):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        # data['id']=model_data.id
        # data["title"]=model_data.title
        # data["content"]=model_data.content
        # data["price"]=model_data.price
        data=model_to_dict(model_data,fields=["id","title","price"])
        return JsonResponse(data)

        # # json_data_str=json.dumps(data)
        # print(data)
        # data=dict(data)
        # json_data_str=json.dumps(data)

        # model instance(model_data)
        # turn a python dict
        # return a json to my_client
    # return JsonResponse(data)
    # return HttpResponse(data,headers={"content_type":"application/json"})
        # return HttpResponse(json_data_str,headers={"content_type":"application/json"})
