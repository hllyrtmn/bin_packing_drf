from .filters import ProductFilter,ProductSearch,CustomOrderingFilter
from products.pagination import CustomPagination
from .models import ProductType, Dimension, WeightType, Product
from .serializers import ProductTypeSerializer, DimensionSerializer, WeightTypeSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from core.views import BaseTrackingViewSet

class ProductViewSet(BaseTrackingViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,CustomOrderingFilter]
    filterset_class = ProductSearch
    
class ProductTypeViewSet(BaseTrackingViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    pagination_class = CustomPagination

class DimensionViewSet(BaseTrackingViewSet):
    queryset = Dimension.objects.all()
    serializer_class = DimensionSerializer
    
class WeightTypeViewSet(BaseTrackingViewSet):
    queryset = WeightType.objects.all()
    serializer_class = WeightTypeSerializer
