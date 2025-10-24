"""
curl -X 'POST'
'http://5.63.153.31:5051/v1/account'
-H 'accept: /'
-H 'Content-Type: application/json'
-d '{
"login": "test_nm",
"email": "testnm@mail.ru",
"password": "12345678"
}'
"""

import requests
import pprint

# url = 'http://5.63.153.31:5051/v1/account'
# headers = {
#     'Accept': '*/*',
#     'Content-Type': 'application/json',
# }
# json = {
#     "login": "test_nm2",
#     "email": "testnm2@mail.ru",
#     "password": "12345678"
# }
#
# response = requests.request("POST", url=url, headers=headers, json=json)
#
# print(response.status_code)
# # pprint.pprint(response.json())
#
# """
# curl -X 'PUT' \
#   'http://5.63.153.31:5051/v1/account/92e847ed-ad87-4d3d-af71-747910029eb4' \
#   -H 'accept: text/plain'
# """

url = 'http://5.63.153.31:5051/v1/account/92e847ed-ad87-4d3d-af71-747910029eb4'
headers = {
    'Accept': 'text/plain'
}

response = requests.request("PUT", url=url, headers=headers)

print(response.status_code)
pprint.pprint(response.json())
response_json = response.json()
print(response_json['resource']['rating']['quantity'])

