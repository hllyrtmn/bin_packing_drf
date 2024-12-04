from rest_framework.viewsets import ModelViewSet
from orders.models import Company
from orders.serializers import CompanySerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer