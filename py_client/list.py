import requests
from getpass import getpass

username = input('What is your username?\n')
password = getpass('What is your password?\n')

auth_endpoint = 'http://localhost:8000/api/auth/'

auth_response = requests.post(auth_endpoint,json={'username':username,'password':password})

if auth_response.status_code == 200:

    token = auth_response.json()['token']
    headers ={
        'Authorization':f'Bearer {token}'#--> default is Token , Bearer is created inside api authentication.py file
    }
    endpoint = 'http://localhost:8000/api/products/'

    list_response = requests.get(endpoint,headers=headers)
    print(list_response.json())