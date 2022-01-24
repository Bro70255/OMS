from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models import CASCADE


class Products(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    payment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Orders(models.Model):
    username = models.CharField(max_length=100)
    products = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=100)
