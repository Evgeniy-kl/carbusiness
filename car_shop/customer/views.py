from django.db.models import QuerySet

from customer.models import Customer, User
from django.shortcuts import get_object_or_404
from customer.serializers import CreateUserSerializer, UserSerializer
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes
from customer.permissions import IsUser


class UserViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin
):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser, ]

    def retrieve(self, request, pk=None):
        queryset = User.objects.all().filter(pk=request.user.id)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
