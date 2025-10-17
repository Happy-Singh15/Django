from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer

class ProductsDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

product_detail_view = ProductsDetailAPIView.as_view()#--> can also be directly used in urls.py of products as view.ProductsDetailAPIView.as_view instead of product_detail_view