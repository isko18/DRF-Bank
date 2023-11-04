from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
import secrets
# Create your models here.

class Users(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    age = models.IntegerField(
        verbose_name='Ваш возраст',
        blank=True, null=True     
    )
    balance = models.IntegerField(
        verbose_name='Баланс',
        blank=True, null=True,
        default=0
    )
    wallet_adress = models.CharField(
        max_length=12,
        verbose_name='Кошелек',
        blank=True, null=True,
        unique=True 
    )

    def __str__(self):
        return self.wallet_adress

    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        if not self.wallet_adress:
            self.wallet_adress = secrets.token_hex(6)
        super().save(*args, **kwargs)