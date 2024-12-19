from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from logistics.models import Pallet
from logistics.serializers import PalletSerializer
from rest_framework.viewsets import ModelViewSet

class PalletViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer
