from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import CustomerAccount


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


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
    image = models.ImageField()
    purchase_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    objects = ProductManager()
    all_objects = models.Manager()

    def delete(self):
        self.is_delete = True
        self.save()

    def hard_delete(self):
        super().delete()

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
