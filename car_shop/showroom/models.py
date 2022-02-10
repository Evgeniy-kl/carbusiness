import django.utils.timezone
from django.db import models
from django_countries.fields import CountryField

from car.models import Car
from core.models import abstract_models


class ShowroomHistory(abstract_models.CreatedAt, abstract_models.AbstractHistory):
    pass


class ShowroomCar(abstract_models.IsActive):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey('Showroom', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.showroom} - {self.car}'


class Location(models.Model):
    country = CountryField(blank_label='(select country)')
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=50)


class Showroom(abstract_models.IsActive, abstract_models.UpdatedAt):
    name = models.CharField(
        verbose_name='Showroom name',
        max_length=100,
        unique=True
    )
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
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
        'ShowroomHistory',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='history'
    )
    current_discount = models.ForeignKey(
        'DiscountShowroom',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class DiscountShowroom(abstract_models.IsActive, abstract_models.AbstractDiscount, abstract_models.CreatedAt):
    pass
