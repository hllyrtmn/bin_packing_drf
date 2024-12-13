from rest_framework import serializers

from products.serializers import DimensionSerializer
from logistics.models import Pallet

class PalletSerializer(serializers.ModelSerializer):
    dimension = DimensionSerializer()
    class Meta:
        model = Pallet
        fields = ['weight','dimension']