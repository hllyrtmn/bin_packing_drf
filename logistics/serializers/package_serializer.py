from rest_framework import serializers

from orders.serializers import OrderSerializer
from logistics.serializers.pallet_serializer import PalletSerializer 
from logistics.models import Package

class PackageSerializer(serializers.ModelSerializer):
    pallet = PalletSerializer()
    order = OrderSerializer()
    class Meta:
        model = Package
        fields = ['pallet','rotation','order']
    def create(self, validated_data):
        
        return super().create(validated_data)

