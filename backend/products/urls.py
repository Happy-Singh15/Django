from django.urls import path

from . import views

urlpatterns = [
    path('',views.alt_api_view),
    path('<int:pk>/', views.alt_api_view),# --> rememeber to add / at the end
]