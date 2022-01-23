from django.shortcuts import render
from .models import Products


def login(request):
    return render(request, 'login.html')


def products(request):
    product_list = Products.objects.all()
    return render(request, 'products.html', {'product_list': product_list})
