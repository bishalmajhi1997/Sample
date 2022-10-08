from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.EventType)
admin.site.register(models.Relation)
admin.site.register(models.Event)
admin.site.register(models.SubEvent)
admin.site.register(models.EventQR)
admin.site.register(models.EventHistory)
admin.site.register(models.EventGift)
admin.site.register(models.UserEvent)
admin.site.register(models.UserAttendance)
admin.site.register(models.EventGreetings)
admin.site.register(models.EventPayment)
admin.site.register(models.EventAttendingQR)
admin.site.register(models.EventImages)
admin.site.register(models.EventHost)
admin.site.register(models.SoloChargeAndTax)
admin.site.register(models.PaymentBreakUp)
admin.site.register(models.UserScan)
admin.site.register(models.EventSpecialGift)
admin.site.register(models.EventVoucher)
