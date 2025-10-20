import requests

product_id = input('what id product you want to delete?\n')

try:
    product_id = int(product_id)
except:
    product_id=None
    print(f'{product_id} is not a valid id.')

if product_id:
    endpoint = f'http://localhost:8000/api/products/{product_id}/delete/'
    delete_response = requests.delete(endpoint)
    if delete_response.status_code==204:
        print(f'product with id {product_id} is deleted.')
    else:
        print(f'product with id {product_id} does not exists.')