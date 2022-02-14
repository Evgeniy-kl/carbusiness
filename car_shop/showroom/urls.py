from showroom.views import ShowroomViewSet, LocationViewSet, ShowroomHistoryViewSet, DiscountShowroomViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'api/showrooms', ShowroomViewSet, basename='showroom')
router.register(r'api/showrooms_location', LocationViewSet, basename='location')
router.register(r'api/showrooms_history', ShowroomHistoryViewSet, basename='show_history')
router.register(r'api/showrooms_discount', DiscountShowroomViewSet, basename='show_discount')

urlpatterns = router.urls

