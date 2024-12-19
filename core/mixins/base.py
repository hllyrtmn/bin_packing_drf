from rest_framework.response import Response
from rest_framework import status

class BaseModelMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)
    
class CreateModelMixin:
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,updated_by = self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UpdateModelMixin:
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user,created_by = self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class DestroyModelMixin:
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)