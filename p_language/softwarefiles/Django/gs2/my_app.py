import requests
import json
print("BISHAL")
URL="http://127.0.0.1:8000/stucreate/"
data={
    'name':'SYousufe',
    'roll':101,
    'city':'Ranchi'
}
print(URL)
json_data=json.dumps(data)
print(json_data)
r=requests.post(url=URL,data=json_data)
print(r)
data=r.json()
print(data)
