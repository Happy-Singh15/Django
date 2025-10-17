import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,json= {"content":"hello world"},params={"id":2})
print(get_response.text)

