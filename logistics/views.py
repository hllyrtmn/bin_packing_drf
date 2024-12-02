from rest_framework.viewsets import ModelViewSet

from core.permissions import IsOwnerOrReadOnly
from .models import Pallet, Package, PackageDetail
from .serializers import PalletSerializer, PackageSerializer, PackageDetailSerializer

class PalletViewSet(ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsOwnerOrReadOnly]

class PackageDetailViewSet(ModelViewSet):
    queryset = PackageDetail.objects.all()
    serializer_class = PackageDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
