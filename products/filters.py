import django_filters
from .models import Product
from products import models
from django.db.models import Q

class ProductFilter(django_filters.FilterSet):
    product_id = django_filters.CharFilter(field_name="id", lookup_expr='icontains')
    code = django_filters.CharFilter(field_name="product_type__code", lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ["id","code"]
        
        
class ProductSearch(django_filters.FilterSet):
    search = django_filters.CharFilter(method='custom_search_filter')

    class Meta:
        model = Product
        fields = []

    def custom_search_filter(self, queryset, name, value):
        """
        Custom search filter to perform search on 'name' and 'product_type__code' fields.
        """
        return queryset.filter(
            Q(id__icontains=value) | Q(product_type__code__icontains=value)
        )