from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class BaseTrackingViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)