from logistics.models import Pallet
from logistics.serializers import PalletSerializer
from core.views import BaseTrackingViewSet

class PalletViewSet(BaseTrackingViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer
