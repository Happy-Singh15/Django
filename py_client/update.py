import requests

endpoint = 'http://localhost:8000/api/products/6/update/'

data= {
    'title':'Hello world using update view'
}

update_response = requests.put(endpoint,json=data)
print(update_response.json())