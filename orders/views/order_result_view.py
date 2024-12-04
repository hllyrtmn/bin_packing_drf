from rest_framework.viewsets import ModelViewSet
from orders.models import OrderResult
from orders.serializers import OrderResultSerializer




class OrderResultViewSet(ModelViewSet):
    queryset = OrderResult.objects.all()
    serializer_class = OrderResultSerializer