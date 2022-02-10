from datetime import datetime

from django.db import models


class IsActive(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)


class CreatedAt(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)


class UpdatedAt(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(auto_now_add=True)


class AbstractHistory(models.Model):
    class Meta:
        abstract = True

    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    showroom = models.ForeignKey('showroom.Showroom', on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=100,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.showroom} - {self.car}'


class AbstractDiscount(models.Model):
    class Meta:
        abstract = True

    discount_percent = models.DecimalField(decimal_places=2, max_digits=4)
    disc_start = models.DateField(
        verbose_name='Discount start at',
        auto_now_add=True,
    )
    disc_end = models.DateField(
        verbose_name='Discount end at',
        auto_now_add=True,
    )
    cars = models.ManyToManyField('car.Car')

    def __str__(self):
        return f'{self.cars} - {self.discount_percent}%'
