#https://httpbin.org/get

import requests

headerdata={"h1":"first header","h2":"second header"}

response = requests.get("https://httpbin.org/get", headers=headerdata)
print(response.text)