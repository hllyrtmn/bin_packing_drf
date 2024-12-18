from core.serializers import BaseTrackingSerializer
from products.serializers import DimensionSerializer
from logistics.models import Truck

class TruckSerializer(BaseTrackingSerializer):
    dimension = DimensionSerializer()
    class Meta:
        model = Truck
        fields = BaseTrackingSerializer.Meta.fields + ['weight_limit','dimension']