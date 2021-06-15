from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Customer
# Register your models here.


class CustomerAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Customer


admin.site.register(Customer, CustomerAdmin)
