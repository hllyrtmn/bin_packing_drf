from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pallet)
admin.site.register(Package)
admin.site.register(PackageDetail)