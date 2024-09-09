from django.db import models
from django_extensions.db.models import TimeStampedModel

from products.models import Product
from users.models import CustomerAccount


class Cart(TimeStampedModel):
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)


class CartItem(TimeStampedModel):
    product_cost = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
