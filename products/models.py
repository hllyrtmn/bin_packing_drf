import uuid
from django.db import models

class ProductType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True, blank=True)

class Dimension(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    width = models.DecimalField(max_digits=15, decimal_places=6)
    height = models.DecimalField(max_digits=15, decimal_places=6)
    depth = models.DecimalField(max_digits=15, decimal_places=6)
    unit = models.CharField(max_length=10)
    volume = models.DecimalField(max_digits=20, decimal_places=10, editable=False)  # Auto-calculated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.volume = self.width * self.height * self.depth
        super().save(*args, **kwargs)

class WeightType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    std = models.DecimalField(max_digits=20, decimal_places=15)
    eco = models.DecimalField(max_digits=20, decimal_places=15)
    pre = models.DecimalField(max_digits=20, decimal_places=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True, blank=True)

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    weight_type = models.ForeignKey(WeightType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True, blank=True)
