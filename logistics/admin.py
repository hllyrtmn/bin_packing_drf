from django.contrib import admin

from core.admin import BaseAdmin
from .models import *
# Register your models here.

@admin.register(Pallet,Package,PackageDetail,Truck)
class LogisticAdmin(BaseAdmin):
    """
    Product admin sınıfı, `BaseAdmin`'i kullanır ve
    `created_by` ve `updated_by` alanlarını otomatik olarak doldurur.
    """