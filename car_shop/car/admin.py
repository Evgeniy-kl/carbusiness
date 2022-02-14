from django.contrib import admin
from car.models import Car, CarManufacturer


@admin.register(Car)
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('features',)


@admin.register(CarManufacturer)
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('name',)
