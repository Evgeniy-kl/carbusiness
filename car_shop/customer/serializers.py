from rest_framework import serializers
from customer.models import User, Customer, Offer


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

