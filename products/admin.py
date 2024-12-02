from django.contrib import admin
from products.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Dimension)
admin.site.register(WeightType)
admin.site.register(ProductType)



