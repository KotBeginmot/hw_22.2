from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users', verbose_name='аватар', **NULLABLE)
    phone_number = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна')
    verification = models.IntegerField(verbose_name='ключ верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
