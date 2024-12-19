from core.serializers import BaseTrackingSerializer
from products.serializers import DimensionSerializer
from logistics.models import Pallet

class PalletSerializer(BaseTrackingSerializer):
    dimension = DimensionSerializer()
    class Meta(BaseTrackingSerializer.Meta):
        model = Pallet
        fields =BaseTrackingSerializer.Meta.fields + ['weight','dimension']