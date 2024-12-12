from rest_framework.viewsets import ModelViewSet

from core.permissions import IsOwnerOrReadOnly
from logistics.models import PackageDetail
from logistics.serializers import PackageDetailSerializer

class PackageDetailViewSet(ModelViewSet):
    queryset = PackageDetail.objects.all()
    serializer_class = PackageDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
