from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Products

def validate_title_no_hello(value):
    qs = Products.objects.filter(title__iexact=value)
    if 'hello' in value.lower():
        raise serializers.ValidationError('hello is not allowed.')
    return value

unique_product_title = UniqueValidator(queryset=Products.objects.all())