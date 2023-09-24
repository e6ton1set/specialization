from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=128)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Empty description")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(default=timezone.now())

    def __str__(self):
        return f"customer: " \
               f"{self.customer}, " \
               f"date: {self.date_ordered}, " \
               f"products: {self.products}," \
               f"total price: {self.total_price}"