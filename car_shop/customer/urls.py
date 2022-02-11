from customer.views import UserViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'api/registration', UserViewSet, basename='user')

urlpatterns = router.urls

