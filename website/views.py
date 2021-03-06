from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Products, Checkout, Orders
from django.contrib import messages
from rest_framework import generics
from .serializers import OrdersSerializers


class Orders_list(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


def index(request):
    orderlist_list = Orders.objects.all()
    return render(request, 'index.html', {'orderlist_list': orderlist_list})


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("products")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def products(request):
    product_list = Products.objects.all()
    return render(request, 'products.html', {'product_list': product_list})


def checkout(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        Checkout.objects.create(user=request.user, product_id=prod_id)
        return redirect('product')
    else:
        return render(request, 'checkout.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect("login")
        else:
            messages.info(request, 'password is not matching')
            return redirect("signup")
    else:
        return render(request, 'signup.html')
