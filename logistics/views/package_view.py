from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from logistics.models import Package
from logistics.serializers import PackageSerializer
from rest_framework.viewsets import ModelViewSet

class PackageViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
