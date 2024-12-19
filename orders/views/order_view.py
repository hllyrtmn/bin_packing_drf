from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet

class OrderViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer