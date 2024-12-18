from logistics.models import Package
from logistics.serializers import PackageSerializer
from core.views import BaseTrackingViewSet

class PackageViewSet(BaseTrackingViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
