import requests
import json

url = "https://reqres.in//api/users/2"

resonse = requests.get(url)
print(resonse.text)

# json_response = json.loads(resonse.text)
# print(json_response)
