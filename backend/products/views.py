from rest_framework import generics,mixins,permissions,authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication

from .models import Products
from .serializers import ProductsSerializer
from .permissions import IsStaffEditorPermission


# Class based views

class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes =[
        authentication.SessionAuthentication,
        TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAdminUser,#--> order of the permissions matter the permission on top will have high priority
        IsStaffEditorPermission,
        # permissions.IsAuthenticatedOrReadOnly #--> (GET Method) will give the access to read the data without authentication
    ]

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


# #Only for List view(get method) but i used create list view which use post as well as get method

# # class ProductsListAPIView(generics.ListAPIView):
# #     queryset = Products.objects.all()
# #     serializer_class = ProductsSerializer

# # product_list_view = ProductsListAPIView.as_view()

class ProductsUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # lookup_field = 'pk' #--> can be changed based on lookup field for database

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance = serializer.save()

product_update_view = ProductsUpdateAPIView.as_view()



class ProductsDestroyAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductsDestroyAPIView.as_view()



#Mixins(similar to function based views but using classes)

# class ProductsMixinView(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
#     ):

#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

#     def get(self,request,*args,**kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request,*args,**kwargs)
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         if kwargs.get('pk'):
#             return self.update(request,*args,**kwargs)# --> should use update in put method but i tried it using in post.
#         return self.create(request,*args,**kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
    
#     def perform_create(self,serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')# or None
#         if content is None:
#             content = "this is perform_create from create mixin"
#         serializer.save(content=content)

#     def perform_update(self, serializer):
#         instance = serializer.save()
#         instance.content = 'this is updated content from mixin'
#         instance = serializer.save()

# product_mixin_view = ProductsMixinView.as_view()



# Function based views

# @api_view(['GET','POST'])
# def alt_api_view(request,pk=None, *args, **kwargs):
    
#     method = request.method
#     if method == 'GET':
#         if pk is not None:
#             # queryset = Products.objects.filter(pk=pk)
#             # if not queryset.exists():
#             #     raise Http404
#             # data = ProductsSerializer(queryset.get()).data
#             # return Response(data)
#             obj = get_object_or_404(Products,pk=pk)
#             data = ProductsSerializer(obj).data
#             return Response(data)
#         queryset = Products.objects.all()
#         data = ProductsSerializer(queryset,many=True).data
#         return Response(data)
#     if method == 'POST':
#         serializer = ProductsSerializer(data=request.data)
#         if serializer.is_valid(raise_exception = True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')# or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({'invalid':'not good data'},status= 400)
        