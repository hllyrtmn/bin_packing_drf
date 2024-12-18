from rest_framework import serializers
from products.serializers import ProductSerializer
from logistics.serializers.package_serializer import PackageSerializer
from logistics.models import PackageDetail
from core.serializers import BaseTrackingSerializer

class PackageDetailSerializer(BaseTrackingSerializer,serializers.ModelSerializer):
    package = PackageSerializer()
    product = ProductSerializer()
    
    class Meta(BaseTrackingSerializer.Meta):
        model = PackageDetail
        fields = BaseTrackingSerializer.Meta.fields + ['package','product','count']
    
    def create(self, validated_data):
        # Product'ı doğrula
        
        return PackageDetail.objects.create(**validated_data)
    
        
