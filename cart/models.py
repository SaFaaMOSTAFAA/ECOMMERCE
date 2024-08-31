from django.db import models

from products.models import Product
from users.models import CustomerAccount


class Cart(models.Model):
    created = models.DateTimeField()
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)


class CartItem(models.Model):
    product_cost = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
