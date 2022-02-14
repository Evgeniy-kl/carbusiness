from supplier.views import SupplierViewSet, SupplierHistoryViewSet, SupplierDiscountViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'api/suppliers', SupplierViewSet, basename='supplier')
router.register(r'api/suppliers_history', SupplierHistoryViewSet, basename='sup-history')
router.register(r'api/suppliers_discount', SupplierDiscountViewSet, basename='sup-discount')

urlpatterns = router.urls