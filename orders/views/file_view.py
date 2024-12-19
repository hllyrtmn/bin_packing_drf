from core.mixins.base import BaseModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from orders.models import File
from orders.serializers import FileSerializer
from rest_framework.viewsets import ModelViewSet

class FileViewSet(BaseModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer