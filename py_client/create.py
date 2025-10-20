import requests
from getpass import getpass

username = input('What is your username?\n')
password = getpass('What is your password?\n')

auth_endpoint = 'http://localhost:8000/api/auth/'

auth_response = requests.post(auth_endpoint,json={'username':username,'password':password})

if auth_response.status_code == 200:

    token = auth_response.json()['token']
    headers ={
        'Authorization':f'Bearer {token}'
        # 'Authorization':'Bearer 26f371cf252e6d36bbd6ce5c6799b83e155ff548'#--> used raw token to emulate the delete token from admin panel
        #--> default is Token , Bearer is created inside api authentication.py file
    }
    endpoint = 'http://localhost:8000/api/products/'


    data = {
        'title':'this is the title'
    }
    create_instance = requests.post(endpoint,json=data,headers=headers)

    print(create_instance.json())