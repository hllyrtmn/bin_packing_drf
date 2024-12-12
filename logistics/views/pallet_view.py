from rest_framework.viewsets import ModelViewSet

from core.permissions import IsOwnerOrReadOnly
from logistics.models import Pallet
from logistics.serializers import PalletSerializer

class PalletViewSet(ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer
    permission_classes = [IsOwnerOrReadOnly]
