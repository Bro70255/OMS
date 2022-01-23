from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('products/', views.products, name='products'),
]
