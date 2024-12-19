from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from logistics.models import Truck
from logistics.serializers import TruckSerializer
from rest_framework.viewsets import ModelViewSet

class TruckViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
