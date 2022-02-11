from rest_framework import serializers
from supplier.models import Supplier, SupplierHistory, DiscountSupplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'foundation']


class SupplierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'foundation', 'showrooms',
                  'sale_history', 'current_discount']


class SupplierHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierHistory
        fields = '__all__'


class DiscountSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountSupplier
        fields = '__all__'
