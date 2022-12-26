# genericcreatelistapiview
import requests
endpoint="http://127.0.0.1:8000/product/create/"
data={"title":"this field is done.","price":33.33}
get_response=requests.post(endpoint)
print(get_response.json())





# genericcreateapiview
# import requests
# endpoint="http://127.0.0.1:8000/product/create/"
# data={"title":"this field is done.","price":33.33}

# get_response=requests.post(endpoint,json=data)
# print(get_response.json())

# genericsretrieveapiview means get
# import requests
# endpoint="http://127.0.0.1:8000/product/1/"#genericretriveapiview
# get_response=requests.get(endpoint)
# print(get_response.json())

# get and post api_view
# import requests
# # endpoint="https://httpbin.org.status/200/"
# # endpoint="https://httpbin.org/anything"
# # endpoint="http://127.0.0.1:8000/"
# endpoint="http://127.0.0.1:8000/product/"

# # get_response=requests.get(endpoint,params={"abc":123},json={"query":"hello world"})#http Request
# # get_response=requests.get(endpoint,json={"product_id":123})#http Request#get
# get_response=requests.post(endpoint,json={"title":"Abc123","content":"hello world","price":99})#http Request#get
# # print(get_response.text)
# print(get_response.headers)
# # HTTP request=HTML
# # REST API HTTP REQUEST=JSON
# # JAVACRIPTS OBJECT NOTATIONS-PYTHON DICT

# print(get_response.json())
# # print(get_response.status_code)

