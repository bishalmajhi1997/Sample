import requests
import json
URL="http://127.0.0.1:8000/studentapi/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
get_data(2)

def post_data():
    data={
    'name':'Manoj',
    'roll':153,
    'city':'BIHAR'
    }

    json_data=json.dumps(data)
    print(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

post_data()

def update_data():

    data={
    'id':1,
    'roll':204,
    'name':'kumar',
    'city':'nok'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

update_data()
def delete_data():
    data={'id':6}

    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
delete_data()
