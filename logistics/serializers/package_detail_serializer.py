from rest_framework import serializers
from products.serializers import ProductSerializer
from logistics.serializers.package_serializer import PackageSerializer
from logistics.models import PackageDetail

class PackageDetailSerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    product = ProductSerializer()
    
    class Meta:
        model = PackageDetail
        fields = ['package','product','count']
    
    def create(self, validated_data):
        # Product'ı doğrula
        
        return PackageDetail.objects.create(**validated_data)
    
        
