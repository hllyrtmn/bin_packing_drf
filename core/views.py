from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class BaseTrackingViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise serializer.ValidationError("You must log in to register.")
        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        if not self.request.user.is_authenticated:
            raise serializer.ValidationError("You must log in to update.")
        serializer.save(updated_by=self.request.user)