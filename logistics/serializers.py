from rest_framework import serializers

from products.serializers import DimensionSerializer
from .models import Pallet, Package, PackageDetail

class PalletSerializer(serializers.ModelSerializer):
    dimension = DimensionSerializer()
    class Meta:
        model = Pallet
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    pallet = PalletSerializer()

    class Meta:
        model = Package
        fields = '__all__'

class PackageDetailSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = PackageDetail
        fields = '__all__'
