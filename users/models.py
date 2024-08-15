from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(regex=r'^\d+$')


class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
