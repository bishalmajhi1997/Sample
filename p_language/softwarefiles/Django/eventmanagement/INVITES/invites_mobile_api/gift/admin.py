from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models


admin.site.register(models.Voucher)
admin.site.register(models.VoucherOption)
admin.site.register(models.SpecialGift)
