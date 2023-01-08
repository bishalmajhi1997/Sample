import requests
import json
url="http://127.0.0.1:8000/"
def get1(values=None):
    data={}
    if values is not None:
        data={"values":values}
    json_data=json.dumps(data)
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)
get1()