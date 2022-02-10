from datetime import datetime

from django.db import models
from car.models import Car
from showroom.models import Showroom
from core.models import abstract_models


class SupplierHistory(abstract_models.CreatedAt, abstract_models.AbstractHistory):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)


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
    cars = models.ManyToManyField(Car, blank=True, null=True)
    sale_history = models.ForeignKey(
        'SupplierHistory',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='history'
    )
    current_discount = models.ForeignKey(
        'DiscountSupplier',
        on_delete=models.CASCADE,
        blank=True,
        null=True,

    )

    def __str__(self):
        return self.name


class DiscountSupplier(abstract_models.IsActive, abstract_models.AbstractDiscount, abstract_models.CreatedAt):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
