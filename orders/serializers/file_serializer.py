from datetime import datetime
from rest_framework import serializers
from orders.models import File, Order
import uuid

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'status', 'uploaded_at', 'order']
        read_only_fields = ['id', 'status', 'uploaded_at', 'order']

    def create(self, validated_data):
        # Varsayılan company_id
        default_company_id = uuid.UUID("3b619a1a-bc3f-42b6-84b8-e312bd984c21")
        # Yeni bir Order oluştur
        order = Order.objects.create(
            company_id=default_company_id,
            date=datetime.now()  # Şu anki tarih ve saati atıyoruz
        )
        # File nesnesini oluştur ve order ile ilişkilendir
        file_instance = File.objects.create(order=order, **validated_data)
        return file_instance