from core.serializers import BaseTrackingSerializer
from orders.serializers import OrderSerializer
from logistics.serializers.pallet_serializer import PalletSerializer 
from logistics.models import Package

class PackageSerializer(BaseTrackingSerializer):
    pallet = PalletSerializer()
    order = OrderSerializer()
    class Meta:
        model = Package
        fields = BaseTrackingSerializer.Meta.fields + ['pallet','rotation','order']
    def create(self, validated_data):
        
        return super().create(validated_data)

