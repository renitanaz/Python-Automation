import requests
import json
import jsonpath

#API URL
url="https://reqres.in/api/users?page=2"

#get response
get_response=requests.get(url)

#converting to json format
json_response =json.loads(get_response.text)
print(json_response)
print("--------------------------")

#fetch value using json path
pages = jsonpath.jsonpath(json_response,'total_pages') #returns list
print(pages)
print("--------------------------")
assert pages[0] == 2  
print("--------------------------")

#advance Json path
first_name=jsonpath.jsonpath(json_response,'data[1].first_name')
print(first_name)

#looping json path

