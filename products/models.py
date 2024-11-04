from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel

from users.models import CustomerAccount


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDelete(models.Model):
    deleted_at = models.DateTimeField(null=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True


class Category(TimeStampedModel, SoftDelete):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(TimeStampedModel, SoftDelete):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(TimeStampedModel, SoftDelete):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    purchase_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

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
