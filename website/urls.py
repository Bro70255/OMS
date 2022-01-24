from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('products/', views.products, name='products'),
    path('logout/', views.logout, name='logout'),
    path('orders/',views.Orders_list.as_view()),
    path('orders/<int:pk>',views.OrderDetails.as_view()),
]