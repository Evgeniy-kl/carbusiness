from django.db import models
from core.models import abstract_models


class CarManufacturer(abstract_models.IsActive, abstract_models.CreatedAt):
    manufacturer_name = models.CharField(verbose_name='Manufacturer', max_length=100, unique=True)

    def __str__(self):
        return self.manufacturer_name


class Car(abstract_models.IsActive, abstract_models.CreatedAt):
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    model = models.CharField(
        verbose_name='Car model',
        max_length=100,
        unique=True
    )
    features = models.JSONField()
    description = models.TextField()

    def __str__(self):
        return f'{self.manufacturer} {self.model}'
