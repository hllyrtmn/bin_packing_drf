from core.serializers import BaseTrackingSerializer
from .models import ProductType, Dimension, WeightType, Product


class ProductTypeSerializer(BaseTrackingSerializer):
    class Meta(BaseTrackingSerializer.Meta):
        model = ProductType
        fields = '__all__'

class DimensionSerializer(BaseTrackingSerializer):
    class Meta(BaseTrackingSerializer.Meta):
        model = Dimension
        fields = ['width','height','depth','unit','volume']

class WeightTypeSerializer(BaseTrackingSerializer):
    class Meta(BaseTrackingSerializer.Meta):
        model = WeightType
        fields = '__all__'

class ProductSerializer(BaseTrackingSerializer):
    product_type = ProductTypeSerializer()
    dimension = DimensionSerializer()
    weight_type = WeightTypeSerializer()

    class Meta(BaseTrackingSerializer.Meta):
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