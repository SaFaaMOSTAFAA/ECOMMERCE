from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(regex=r'^\d+$')


class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_validator], max_length=25)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
