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
# get1(3)


def post1():
    data={"id":10,"name":"maghav","roll":112,"city":"MUMBAI_PUNE"}
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)
# post1()
def update1():
    data={"id":7,"name":"Balajeee","roll":109,"city":"BBSR"}
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)
# update1()

def delete1():
   data={"id":7}
   json_data=json.dumps(data)
   r=requests.delete(url=url,data=json_data)
   data=r.json()
   print(data)
# delete1()

