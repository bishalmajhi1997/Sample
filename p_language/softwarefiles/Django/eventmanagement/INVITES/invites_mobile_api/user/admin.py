from django.contrib import admin

# Register your models here.
"""Register your models here."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUsrAdmin
from django.utils.translation import gettext_lazy as _
from user import models
from .forms import UserCreationForm, UserChangeForm, SMSDeviceForm


class UserAdmin(BaseUsrAdmin):
    """UserAdmin class extracted from auth UserAdmin"""
    ordering = ('id',)
    add_form = UserCreationForm
    form = UserChangeForm
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', "is_admin", "department")
    list_display = ('__str__', 'first_name', 'last_name', 'is_staff', "department")
    search_fields = ('first_name', 'last_name', 'phone', "email", "department")
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', "email",)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),
        (_('Personal info'), {
            'fields': ("address_line_1", "address_line_2",
                       "state", "country", "city", "department", "is_admin", "image"),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', "email", "address_line_1", "address_line_2",
                       "state", "country", "city", "department", "is_admin", 'password1', 'password2'),
        }),
    )

class SMSDeviceAdmin(admin.ModelAdmin):
    form = SMSDeviceForm

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Card)
admin.site.register(models.BankDetail)
admin.site.register(models.SMSDevice, SMSDeviceAdmin)
