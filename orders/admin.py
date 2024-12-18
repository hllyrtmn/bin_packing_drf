from django.contrib import admin

from core.admin import BaseAdmin
from orders.models import *

# Register your models here.


@admin.register(Company,Order,OrderDetail,OrderResult,File)
class OrderAdmin(BaseAdmin):
    """
    Product admin sınıfı, `BaseAdmin`'i kullanır ve
    `created_by` ve `updated_by` alanlarını otomatik olarak doldurur.
    """