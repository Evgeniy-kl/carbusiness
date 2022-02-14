from showroom.models import Showroom, ShowroomHistory, DiscountShowroom, Location
from rest_framework import serializers


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ['name', 'location', 'features', 'balance']


class ShowroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ['name', 'location', 'features',
                  'balance', 'cars', 'unique_customers',
                  'sale_history', 'current_discount']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ShowroomHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomHistory
        fields = '__all__'


class DiscountShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShowroom
        fields = '__all__'
