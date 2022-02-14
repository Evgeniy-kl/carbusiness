from django.contrib import admin
from supplier.models import Supplier, SupplierHistory, DiscountSupplier


@admin.register(Supplier)
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('foundation', 'showrooms',)


@admin.register(SupplierHistory, DiscountSupplier)
class DefaultAdmin(admin.ModelAdmin):
    list_filter = ('supplier',)
