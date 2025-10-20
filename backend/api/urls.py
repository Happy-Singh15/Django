from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

# from .views import api_home

urlpatterns= [
    #path('',api_home),
    path('auth/',obtain_auth_token),
    path('products/',include('products.urls'))#--> can also be included in cfehome urls directly with another endpoint 
]