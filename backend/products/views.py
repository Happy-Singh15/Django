from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer


class ProductsListCreateAPIView(generics.ListCreateAPIView):
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

product_list_create_view = ProductsListCreateAPIView.as_view()

class ProductsDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

product_detail_view = ProductsDetailAPIView.as_view()#--> can also be directly used in urls.py of products as view.ProductsDetailAPIView.as_view instead of product_detail_view


#Only for List view(get method) but i used create list view which use post as well as get method

# class ProductsListAPIView(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

# product_list_view = ProductsListAPIView.as_view()