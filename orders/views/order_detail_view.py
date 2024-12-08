from rest_framework.viewsets import ModelViewSet
from orders.models import OrderDetail
from orders.serializers import OrderDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from orders.filters import OrderDetailFilter


class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = OrderDetailFilter