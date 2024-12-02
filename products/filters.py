import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    product_id = django_filters.CharFilter(field_name="id", lookup_expr='icontains')
    code = django_filters.CharFilter(field_name="product_type__code", lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ["id","code"]