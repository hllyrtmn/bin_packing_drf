from orders.models import Company
from orders.serializers import CompanySerializer
from core.views import BaseTrackingViewSet

class CompanyViewSet(BaseTrackingViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer