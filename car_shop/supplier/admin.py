from django.contrib import admin
from supplier.models import Supplier, SupplierHistory, DiscountSupplier

admin.site.register(Supplier)
admin.site.register(SupplierHistory)
admin.site.register(DiscountSupplier)
