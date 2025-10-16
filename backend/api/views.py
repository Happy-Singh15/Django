from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from products.models import Products
def api_home(request, *args, **kwargs):
    model_data = Products.objects.all().order_by('?').first()
    data={}
    if model_data:
        # without using model_to_dict

        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # using model_to_dict
        data = model_to_dict(model_data,fields=['id','title','price'])
    return JsonResponse(data)

