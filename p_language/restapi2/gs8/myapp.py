import requests
import json
url="http://127.0.0.1:8000/"
def get1(id=None):
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)
# get1(6)


def post1():
    data={"name":"rohan","roll":123,"city":"ranchi"}
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)
post1()
def update1():
    data={"id":7,"name":"mohan","roll":103,"city":"BBSR"}
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)
# update1()

def delete1():
   data={"id":6}
   json_data=json.dumps(data)
   r=requests.delete(url=url,data=json_data)
   data=r.json()
   print(data)
# delete1()

