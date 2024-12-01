from rest_framework.viewsets import ModelViewSet
from .models import ProductType, Dimension, WeightType, Product
from .serializers import ProductTypeSerializer, DimensionSerializer, WeightTypeSerializer, ProductSerializer

class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class DimensionViewSet(ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer

class WeightTypeViewSet(ModelViewSet):
    queryset = WeightType.objects.all()
    serializer_class = WeightTypeSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
