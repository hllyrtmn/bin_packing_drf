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
        
    def create(self, validated_data):
        # Nested veriyi ayıklayın
        product_type_data = validated_data.pop('product_type')
        dimension_data = validated_data.pop('dimension')
        weight_type_data = validated_data.pop('weight_type')

        # Nested modelleri oluşturun veya alın
        product_type = ProductType.objects.create(**product_type_data)
        dimension = Dimension.objects.create(**dimension_data)
        weight_type = WeightType.objects.create(**weight_type_data)

        # Ana modeli oluşturun
        product = Product.objects.create(
            product_type=product_type,
            dimension=dimension,
            weight_type=weight_type,
            **validated_data
        )
        return product