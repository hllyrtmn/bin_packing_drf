from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from orders.models import Company
from orders.serializers import CompanySerializer
from rest_framework.viewsets import ModelViewSet

class CompanyViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer