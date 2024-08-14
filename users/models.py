from django.contrib.auth.hashers import make_password
from django.db import models


class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
