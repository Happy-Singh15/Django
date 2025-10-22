from rest_framework import serializers

from .models import Products
from . import validators

class ProductsSerializer(serializers.ModelSerializer):
    my_discount  = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[
        validators.validate_title_no_hello,
        validators.unique_product_title])
    class Meta:
        model = Products
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Products):
            return None
        return obj.get_discount()
        