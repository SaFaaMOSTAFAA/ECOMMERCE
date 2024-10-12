from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import CustomerAccount


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    purchase_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class ProductReview(TimeStampedModel):
    review = models.TextField()
    rate = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)


class WishList(TimeStampedModel):
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
