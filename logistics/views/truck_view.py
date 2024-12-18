from logistics.models import Truck
from logistics.serializers import TruckSerializer
from core.views import BaseTrackingViewSet

class TruckViewSet(BaseTrackingViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
