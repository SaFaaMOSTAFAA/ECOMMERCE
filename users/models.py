from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(regex=r'^\d+$')


class AdminManager(BaseUserManager):
    def create_user(self, user_name, password=None, **extra_fields):
        if not user_name:
            raise ValueError('The Username field must be set')
        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_name, password, **extra_fields)


class Admin(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[phone_validator], max_length=25)
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['full_name', 'phone']

    def __str__(self):
        return self.user_name
