from django.db import models
from django.contrib.auth.models import User

class BaseTrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        related_name='%(class)s_created',
        null=True
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        related_name='%(class)s_updated',
        null=True
    )
    is_deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # `request` objesini kwargs'dan al
        if request:
            if not self.pk:  # Yeni bir nesne oluşturuluyorsa
                self.created_by = request.user
            self.updated_by = request.user
        super().save(*args, **kwargs)