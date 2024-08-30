from django.db import models

from products.models import Product
from users.models import CustomerAccount


class Cart(models.Model):
    created = models.DateTimeField()
    customer_id = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)


class CartItem(models.Model):
    product_cost = models.FloatField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
