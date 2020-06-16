import requests
import json
baseURL = 'https://reqres.in//api//users'
parameters = {'page':'2'}
response =requests.get(baseURL,params=parameters )
content_in_response = response.content
print(response.text)
#info = json.loads(response.text)
#print(type(info))
#print(info)
