import requests
# endpoint="https://httpbin.org.status/200/"
# endpoint="https://httpbin.org/anything"
# endpoint="http://127.0.0.1:8000/"
endpoint="http://127.0.0.1:8000/product/"

# get_response=requests.get(endpoint,params={"abc":123},json={"query":"hello world"})#http Request
get_response=requests.get(endpoint,json={"product_id":123})#http Request
print(get_response.text)
print(get_response.headers)
# HTTP request=HTML
# REST API HTTP REQUEST=JSON
# JAVACRIPTS OBJECT NOTATIONS-PYTHON DICT

# print(get_response.json())
# print(get_response.status_code)

