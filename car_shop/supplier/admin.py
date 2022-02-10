from django.contrib import admin
from supplier.models import Supplier, SupplierHistory, DiscountSupplier


@admin.register(Supplier, SupplierHistory, DiscountSupplier)
class DefaultAdmin(admin.ModelAdmin):
    pass
