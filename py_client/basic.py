import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint,json= {"id":1},params={"id":2})
print(get_response.json())

