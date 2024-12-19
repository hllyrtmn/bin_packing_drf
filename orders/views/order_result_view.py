from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from orders.models import OrderResult
from orders.serializers import OrderResultSerializer
from rest_framework.viewsets import ModelViewSet



class OrderResultViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = OrderResult.objects.all()
    serializer_class = OrderResultSerializer