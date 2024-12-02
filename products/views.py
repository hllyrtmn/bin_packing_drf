from rest_framework.viewsets import ModelViewSet

from products.pagination import CustomPagination
from .models import ProductType, Dimension, WeightType, Product
from .serializers import ProductTypeSerializer, DimensionSerializer, WeightTypeSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type','dimension','weigth_type']

class DimensionViewSet(ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    
class WeightTypeViewSet(ModelViewSet):
    queryset = WeightType.objects.all()
    serializer_class = WeightTypeSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
