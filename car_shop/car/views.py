from car.models import Car, CarManufacturer
from django.shortcuts import get_object_or_404
from car.serializers import CarSerializer, CarManufacturerSerializer
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class CarViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['manufacturer__name', 'features', ]


class CarManufacturerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = CarManufacturerSerializer
    queryset = CarManufacturer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

