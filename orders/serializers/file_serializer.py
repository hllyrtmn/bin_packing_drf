from datetime import datetime
from core.serializers import BaseTrackingSerializer
from orders.models import File, Order
import uuid

class FileSerializer(BaseTrackingSerializer):
    class Meta(BaseTrackingSerializer.Meta):
        model = File
        fields = ['id', 'file', 'order']
        read_only_fields = ['id', 'order']

    def create(self, validated_data):
        # Varsayılan company_id
        default_company_id = uuid.UUID("9bbb2ba0-d55d-4537-a95d-a878715478c3")
        # Yeni bir Order oluştur
        order = Order.objects.create(
            company_id=default_company_id,
            date=datetime.now()  # Şu anki tarih ve saati atıyoruz
        )
        # File nesnesini oluştur ve order ile ilişkilendir
        file_instance = File.objects.create(order=order, **validated_data)
        return file_instance