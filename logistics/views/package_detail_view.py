from logistics.models import PackageDetail
from logistics.serializers import PackageDetailSerializer
from core.views import BaseTrackingViewSet

class PackageDetailViewSet(BaseTrackingViewSet):
    queryset = PackageDetail.objects.all()
    serializer_class = PackageDetailSerializer
