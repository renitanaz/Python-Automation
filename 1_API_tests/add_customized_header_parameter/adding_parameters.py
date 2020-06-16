import requests

parameters = {"P1":"parameters1", "P2":"parameter2"}

response = requests.get("https://httpbin.org/get", params=parameters)
print(response.text)