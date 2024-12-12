from rest_framework.viewsets import ModelViewSet

from core.permissions import IsOwnerOrReadOnly
from logistics.models import Package
from logistics.serializers import PackageSerializer

class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsOwnerOrReadOnly]
