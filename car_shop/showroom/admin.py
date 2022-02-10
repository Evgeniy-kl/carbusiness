from django.contrib import admin
from showroom.models import Showroom, ShowroomHistory, DiscountShowroom, Location


@admin.register(Showroom, ShowroomHistory, DiscountShowroom, Location)
class DefaultAdmin(admin.ModelAdmin):
    pass
