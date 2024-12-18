from orders.models import Order
from orders.serializers import OrderSerializer
from core.views import BaseTrackingViewSet

class OrderViewSet(BaseTrackingViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer