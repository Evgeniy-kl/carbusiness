import django.utils.timezone
from django.db import models
from django_countries.fields import CountryField

from car.models import Car
from core.models import abstract_models


class ShowroomHistory(abstract_models.CreatedAt):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom_name = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=100,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.showroom_name} - {self.car}'


class ShowroomCar(abstract_models.IsActive):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.showroom} - {self.car}'


class Showroom(abstract_models.IsActive, abstract_models.UpdatedAt):
    name = models.CharField(
        verbose_name='Showroom name',
        max_length=100,
        unique=True
    )
    location = CountryField(blank_label='(select country)')
    features = models.JSONField()
    cars = models.ManyToManyField(
        Car,
        through='ShowroomCar',
        blank=True,
        null=True
    )
    balance = models.DecimalField(
        verbose_name='Balance',
        decimal_places=2,
        max_digits=100
    )
    unique_customers = models.ManyToManyField(
        'customer.Customer',
        blank=True,
        null=True
    )
    sale_history = models.ForeignKey(
        ShowroomHistory,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    current_discount = models.ForeignKey(
        'DiscountShowroom',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class DiscountShowroom(abstract_models.IsActive):
    discount_percent = models.DecimalField(decimal_places=2, max_digits=4)
    disc_start = models.DateField(
        verbose_name='Discount start at',
        default=django.utils.timezone.now()
    )
    disc_end = models.DateField(
        verbose_name='Discount end at',
        default=django.utils.timezone.now()
    )
    cars = models.ManyToManyField(Car)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.cars} - {self.discount_percent}%'
