from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from logistics.models import PackageDetail
from logistics.serializers import PackageDetailSerializer
from rest_framework.viewsets import ModelViewSet

class PackageDetailViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = PackageDetail.objects.all()
    serializer_class = PackageDetailSerializer
