from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from car.models import Car
from core.models import abstract_models

User = get_user_model()


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=20)
    surname = models.CharField(verbose_name='Surname', max_length=20)
    patronymic = models.CharField(verbose_name='Patronymic', max_length=20)
    phoneNumber = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    balance = models.DecimalField(
        verbose_name='Balance',
        decimal_places=2,
        max_digits=100
    )
    buy_history = models.ManyToManyField(
        'CustomerHistory',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'


class CustomerHistory(abstract_models.CreatedAt):
    offer = models.OneToOneField('Offer', on_delete=models.CASCADE, primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=100,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.customer_name} - {self.car}'


class Offer(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car_name = models.ForeignKey(Car, on_delete=models.CASCADE, default=1)
    car_price = models.DecimalField(
        verbose_name='Car price',
        max_digits=100,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.user}'s offer"
