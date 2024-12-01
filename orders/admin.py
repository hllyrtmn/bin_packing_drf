from django.contrib import admin

from orders.models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(OrderResult)