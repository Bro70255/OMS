from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]