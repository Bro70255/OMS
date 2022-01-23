from django.shortcuts import render
from django.contrib import messages
from .models import Products

from .forms import CustomUserForm


def products(request):
    product_list = Products.objects.all()
    return render(request, 'products.html', {'product_list': product_list})


def checkout(request):
    return render(request, 'checkout.html')


def login(request):
    form = CustomUserForm()
    context = {"form": form}
    return render(request, 'login.html',context)
