import requests

endpoint = 'http://localhost:8000/api/products/'


list_response = requests.get(endpoint)
print(list_response.json())