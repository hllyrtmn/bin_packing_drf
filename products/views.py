from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter,ProductSearch,CustomOrderingFilter
from products.pagination import CustomPagination
from .models import ProductType, Dimension, WeightType, Product
from .serializers import ProductTypeSerializer, DimensionSerializer, WeightTypeSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser
from core.permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,CustomOrderingFilter]
    filterset_class = ProductSearch
    permission_classes = [IsOwnerOrReadOnly]
    
class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    pagination_class = CustomPagination
    permission_classes = [IsOwnerOrReadOnly]

class DimensionViewSet(ModelViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class WeightTypeViewSet(ModelViewSet):
    queryset = WeightType.objects.all()
    serializer_class = WeightTypeSerializer
    permission_classes = [IsOwnerOrReadOnly]
