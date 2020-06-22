from django.contrib import admin


from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Client,Admin

# Register your models here.
@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'paid_until','created_on','on_trial')

admin.site.register(Admin)