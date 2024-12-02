from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from products.pagination import CustomPagination
from .models import ProductType, Dimension, WeightType, Product
from .serializers import ProductTypeSerializer, DimensionSerializer, WeightTypeSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from core.permissions import IsOwnerOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    permission_classes = [IsOwnerOrReadOnly]
    
class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    pagination_class = CustomPagination

class DimensionViewSet(ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    
class WeightTypeViewSet(ModelViewSet):
    queryset = WeightType.objects.all()
    serializer_class = WeightTypeSerializer

