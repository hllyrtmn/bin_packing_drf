from orders.models import OrderResult
from orders.serializers import OrderResultSerializer
from core.views import BaseTrackingViewSet



class OrderResultViewSet(BaseTrackingViewSet):
    queryset = OrderResult.objects.all()
    serializer_class = OrderResultSerializer