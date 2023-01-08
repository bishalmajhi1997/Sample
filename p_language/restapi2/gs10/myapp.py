import requests
import json
url="http://127.0.0.1:8000/"
def get1(id=None):
    data={}
    if id is not None:
        data={"id":id}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=url,data=json_data,headers=headers)
    data=r.json()
    print(data)
# get1(2)


def post1():
    data={"name":"rohan","roll":123,"city":"ranchi"}
    headers={'content-Type':'application/json'}

    json_data=json.dumps(data)
    # headers={'content-Type':'application/json'}
    r=requests.post(url=url,data=json_data,headers=headers)
    data=r.json()
    print(data)
# post1()
def update1():
    data={"id":4,"name":"mohan","roll":4,"city":"BBSR"}
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data,headers=headers)
    data=r.json()
    print(data)
# update1()

def delete1():
   data={"id":3}
   headers={'content-Type':'application/json'}
   json_data=json.dumps(data)
   r=requests.delete(url=url,data=json_data,headers=headers)
   data=r.json()
   print(data)
delete1()

