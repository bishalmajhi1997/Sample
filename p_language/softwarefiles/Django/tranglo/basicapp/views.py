from django.shortcuts import render
from rest_framework import decorators
from tranglo.settings import UID,PWD,SECRET_KEY
from rest_framework.decorators import api_view
from shortuuid import ShortUUID
from rest_framework.response import Response
import hashlib
import requests
import json

# Create your views here.
@api_view(['GET'])
def trangloview(request):
    userid=UID
    userpassword=PWD
    key=SECRET_KEY
    url="http://staging-gloremit.tranglo.com:2014/v1/payments/validation"
    transid=ShortUUID().random(length=12)
    #print(userid,userpassword,key,url,transid)
    transID=transid
    sIdType=1
    sIdNum="000000"
    sFirstName="Test1"
    sLastName="Ting2"
    bFirstName="Bishal"
    bLastName="Kumar"
    bCountry="ID"
    bAccType=1
    bIssuerCode="002"
    bAccNum="376800000000888"
    trxValue=100000
    params={"transID":transID,"sIdType":sIdType,"sIdNum":sIdNum,"sFirstName":sFirstName,"sLastName":sLastName,
             "bFirstName":bFirstName,"bLastName":bLastName,"bCountry":bCountry,"bAccType":bAccType,"bIssuerCode":bIssuerCode,
             "bAccNum":bAccNum,"trxValue":trxValue}
    concatenate=userid+transID+sIdNum+str(bAccType)+bAccNum+bIssuerCode+key
    print(concatenate)
    result = hashlib.md5(concatenate.encode())
    #print(result.hexadigest())
    print(result.hexdigest())
    Authorization= "GLOREMIT {UID}:{PWD}:{rspSign}".format(UID=userid,PWD=userpassword,rspSign=result.hexdigest())
    print(Authorization)
    #response_API = requests.get(url)
    #print(response_API)
    headers_dict = {"Authorization": Authorization}
    response = requests.get(url,headers=headers_dict,params=params)
    print(response.__dict__)
    json_data = json.loads(response.text)
    #print(json_data)

    return Response(json_data)
