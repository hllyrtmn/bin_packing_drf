from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from core.permissions import IsCompanyMember
from orders.models import Company, Order
from orders.serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet

class OrderViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsCompanyMember]
    
    def get_queryset(self):
        
        return Order.objects.filter(company__users=self.request.user, is_deleted=False)