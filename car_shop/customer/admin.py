from django.contrib import admin
from customer.models import Customer, CustomerHistory, Offer


@admin.register(Customer, )
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('balance',)


@admin.register(Offer, )
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(CustomerHistory, )
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('customer_name',)


