from django.contrib import admin
from customer.models import Customer, CustomerHistory, Offer


@admin.register(Customer, CustomerHistory, Offer)
class DefaultAdmin(admin.ModelAdmin):
    pass
