from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer


class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self,serializer):
        # serializer.save(user=self.request.user) #--> will use in future
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')# or None
        if content is None:
            content = title
        serializer.save(content=content)
        # can be used to send a signal using django

product_create_view = ProductsCreateAPIView.as_view()

class ProductsDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

product_detail_view = ProductsDetailAPIView.as_view()#--> can also be directly used in urls.py of products as view.ProductsDetailAPIView.as_view instead of product_detail_view