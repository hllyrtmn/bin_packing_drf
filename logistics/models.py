import uuid
from django.db import models
from orders.models import Order  # ForeignKey için import
from products.models import Product, Dimension  # Pallet ve paket boyutları için
from core.models import BaseTrackingModel

class Pallet(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

class Truck(BaseTrackingModel):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    dimension = models.ForeignKey(Dimension,on_delete=models.CASCADE)
    weight_limit = models.DecimalField(max_digits=10,decimal_places=2)
    
class Package(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    pallet = models.ForeignKey(Pallet, on_delete=models.SET_NULL, null=True, blank=True, related_name='pallets')

class PackageDetail(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='packages')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()