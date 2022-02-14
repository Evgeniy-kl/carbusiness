from django.contrib import admin
from showroom.models import Showroom, ShowroomHistory, DiscountShowroom, Location


@admin.register(Showroom)
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('features',)
    ordering = ('features', )


@admin.register(Location)
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('country', 'city')


@admin.register(ShowroomHistory, DiscountShowroom)
class DefaultAdmin(admin.ModelAdmin):
    filter_fields = ('showroom',)
