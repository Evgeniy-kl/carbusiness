from car.views import CarViewSet, CarManufacturerViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'api/cars', CarViewSet, basename='car')
router.register(r'api/cars_brand', CarManufacturerViewSet, basename='car_brand')

urlpatterns = router.urls
