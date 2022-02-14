from rest_framework.permissions import AllowAny
from supplier.serializers import SupplierSerializer, SupplierHistorySerializer, DiscountSupplierSerializer, \
    SupplierListSerializer
from supplier.models import Supplier, SupplierHistory, DiscountSupplier
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework import filters


class SupplierViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializers = {'list': SupplierListSerializer,
                   'retrieve': SupplierListSerializer}
    serializer_class = SupplierSerializer
    permission_classes = [AllowAny, ]
    queryset = Supplier.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['cars__model', ]
    ordering_fields = ['foundation', ]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class SupplierHistoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = SupplierHistorySerializer
    permission_classes = [AllowAny, ]
    queryset = SupplierHistory.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['supplier__name', ]


class SupplierDiscountViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = DiscountSupplierSerializer
    permission_classes = [AllowAny, ]
    queryset = DiscountSupplier.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['supplier__name', ]
    ordering_fields = ['disc_start']
