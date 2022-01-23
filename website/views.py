from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Products
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("products")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def products(request):
    product_list = Products.objects.all()
    return render(request, 'products.html', {'product_list': product_list})


def checkout(request):
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
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect("login")
        else:
            messages.info(request, 'password is not matching')
            return redirect("signup")
    else:
        return render(request, 'signup.html')
