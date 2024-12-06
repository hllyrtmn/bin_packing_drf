
import django_filters
from orders.models import OrderDetail


class OrderDetailFilter(django_filters.FilterSet):
    order_id = django_filters.CharFilter(field_name="order__id", lookup_expr='icontains')
    
    class Meta:
        model = OrderDetail
        fields = ["order_id"]