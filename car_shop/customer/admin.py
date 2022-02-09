from django.contrib import admin
from customer.models import Customer, CustomerHistory, Offer

admin.site.register(Customer)
admin.site.register(CustomerHistory)
admin.site.register(Offer)
