from rest_framework.viewsets import ModelViewSet
from orders.models import File
from orders.serializers import FileSerializer
from rest_framework.permissions import AllowAny

class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [AllowAny]