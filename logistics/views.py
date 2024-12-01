from rest_framework.viewsets import ModelViewSet
from .models import Pallet, Package, PackageDetail
from .serializers import PalletSerializer, PackageSerializer, PackageDetailSerializer

class PalletViewSet(ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer

class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class PackageDetailViewSet(ModelViewSet):
    queryset = PackageDetail.objects.all()
    serializer_class = PackageDetailSerializer
