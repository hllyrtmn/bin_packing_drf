from rest_framework.viewsets import ModelViewSet
from orders.models import OrderDetail
from orders.serializers import OrderDetailSerializer

class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer