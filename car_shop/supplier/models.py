from datetime import datetime

from django.db import models
import django.utils.timezone
from car.models import Car
from showroom.models import Showroom
from core.models import abstract_models


class Supplier(abstract_models.IsActive, abstract_models.CreatedAt, abstract_models.UpdatedAt):
    name = models.CharField(
        verbose_name='Supplier name',
        max_length=100,
        unique=True
    )
    foundation = models.DateField(
        verbose_name='Foundation date',
        default=datetime.now().year,
        blank=True
    )
    showrooms = models.ManyToManyField(
        Showroom,
        blank=True,
        null=True
    )
    cars = models.ManyToManyField(Car)
    deal_history = models.ManyToManyField(
        'SupplierHistory',
        blank=True,
        null=True
    )
    current_discount = models.ManyToManyField(
        'DiscountSupplier',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name}'


class SupplierHistory(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=100,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.showroom} - {self.car}'


class DiscountSupplier(abstract_models.IsActive):
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

    def __str__(self):
        return f'{self.cars} - {self.discount_percent}%'
