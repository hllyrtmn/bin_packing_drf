from django.contrib import admin
from core.admin import BaseAdmin
from products.models import *
# Register your models here.
# admin.site.register(Product)
# admin.site.register(Dimension)
# admin.site.register(WeightType)
# admin.site.register(ProductType)

@admin.register(ProductType,Product,Dimension,WeightType)
class ProductAdmin(BaseAdmin):
    """
    Product admin sınıfı, `BaseAdmin`'i kullanır ve
    `created_by` ve `updated_by` alanlarını otomatik olarak doldurur.
    """