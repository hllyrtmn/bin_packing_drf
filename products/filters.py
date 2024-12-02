import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_width = django_filters.NumberFilter(field_name="dimension__width", lookup_expr='gte')
    max_width = django_filters.NumberFilter(field_name="dimension__width", lookup_expr='lte')
    min_height = django_filters.NumberFilter(field_name="dimension__height", lookup_expr='gte')
    max_height = django_filters.NumberFilter(field_name="dimension__height", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['product_type', 'weight_type', 'min_width', 'max_width', 'min_height', 'max_height']
