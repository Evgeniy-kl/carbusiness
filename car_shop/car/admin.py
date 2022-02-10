from django.contrib import admin
from car.models import Car, CarManufacturer


@admin.register(Car, CarManufacturer)
class DefaultAdmin(admin.ModelAdmin):
    pass
