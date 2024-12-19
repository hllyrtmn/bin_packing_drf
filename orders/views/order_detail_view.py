from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from orders.models import OrderDetail
from orders.serializers import OrderDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from orders.filters import OrderDetailFilter
from rest_framework.viewsets import ModelViewSet

class OrderDetailViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = OrderDetailFilter