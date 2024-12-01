from rest_framework import serializers
from .models import ProductType, Dimension, WeightType, Product

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = '__all__'

class WeightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightType
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()
    dimension = DimensionSerializer()
    weight_type = WeightTypeSerializer()

    class Meta:
        model = Product
        fields = '__all__'
