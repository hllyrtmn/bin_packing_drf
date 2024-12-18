from orders.models import File
from orders.serializers import FileSerializer
from core.views import BaseTrackingViewSet

class FileViewSet(BaseTrackingViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer