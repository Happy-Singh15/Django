import requests

endpoint = 'http://localhost:8000/api/products/'


data = {
    'title':'this is the title'
}
create_instance = requests.post(endpoint,json=data)

print(create_instance.json())