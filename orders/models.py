import uuid
from django.db import models
from products.models import Product  # ForeignKey için import
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import BaseTrackingModel

class CompanyUser(BaseTrackingModel):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='company_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_companies')

    class Meta:
        db_table = 'orders_company_users' 
        unique_together = ('company', 'user')  # Aynı kullanıcı aynı şirkete birden fazla kez atanamaz.


class Company(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User,related_name='companies',through='CompanyUser',through_fields=('company', 'user'))
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Order(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField()

class OrderDetail(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.count * self.unit_price
        super().save(*args, **kwargs)

class OrderResult(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='results')
    result = models.TextField()
    success = models.BooleanField(default=False)
    progress = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    
class File(BaseTrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='files', null=True, blank=True)
    file = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return f"File {self.id} for Order {self.order.id if self.order else 'No Order'}"
