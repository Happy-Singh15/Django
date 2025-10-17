# from django.http import JsonResponse #--> without using django rest framework
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Products

# @api_view(['POST']) #--> will throw error {"detail":"Method \"GET\" not allowed."} and status code 405
# @api_view(['GET','POST']) --> can be used for multiple methods
@api_view(['GET'])#--> will get the data
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
    return Response(data)# --> will use JsonResponse without using django rest framework

