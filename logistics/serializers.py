from rest_framework import serializers

from orders.serializers import OrderSerializer
from products.models import Product
from products.serializers import DimensionSerializer, ProductSerializer
from .models import Pallet, Package, PackageDetail

class PalletSerializer(serializers.ModelSerializer):
    dimension = DimensionSerializer()
    class Meta:
        model = Pallet
        fields = ['weight','dimension']
        

class PackageSerializer(serializers.ModelSerializer):
    pallet = PalletSerializer()
    order = OrderSerializer()
    class Meta:
        model = Package
        fields = ['pallet','rotation','order']
    def create(self, validated_data):
        
        return super().create(validated_data)

class PackageDetailSerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    product = ProductSerializer()
    
    class Meta:
        model = PackageDetail
        fields = ['package','product','count']
    
    def create(self, validated_data):
        # Product'ı doğrula
        
        return PackageDetail.objects.create(**validated_data)
    
        
