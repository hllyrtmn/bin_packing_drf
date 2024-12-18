from rest_framework import serializers

from products.serializers import DimensionSerializer
from logistics.models import Truck

class TruckSerializer(serializers.ModelSerializer):
    dimension = DimensionSerializer()
    class Meta:
        model = Truck
        fields = ['weight_limit','dimension']