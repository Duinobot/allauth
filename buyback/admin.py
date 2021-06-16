from django.contrib import admin
from django.dispatch.dispatcher import receiver
from import_export.admin import ImportExportMixin
from .models import Buyback, Exchange, BuybackItem, ExchangeItem, SendList

from django.utils import timezone

from django.db.models.signals import pre_save, post_save

# Register your models here.


class BuybackAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Buyback
    list_display = ['name', 'price']
    search_fields = ['name']


class ExchangeAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Exchange
    list_display = ['name', 'price']
    search_fields = ['name']


class BuybackItemTabularInline(admin.TabularInline):
    model = BuybackItem


class ExchangeItemTabularInline(admin.TabularInline):
    model = ExchangeItem


class SendListAdmin(ImportExportMixin, admin.ModelAdmin):
    model = SendList
    inlines = [
        BuybackItemTabularInline,
        ExchangeItemTabularInline,
    ]
    readonly_fields = ('modifier', 'created_date', 'modified_date',)
    list_display = ['order_id', 'status', 'customer', 'created_date',
                    'modified_date', ]
    search_fields = ['order_id', 'customer__first_name',
                     'customer__last_name', 'customer__username', 'customer__email']
    list_filter = ['status']
    fieldsets = [
        ('Order', {'fields': [
         ('order_id', 'customer'), ('created_date', 'modified_date', 'modifier')]}),
        ('Status', {'fields': [
         'status']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.modified_date = timezone.now()
        obj.modifier = request.user
        super().save_model(request, obj, form, change)
        if not obj.customer:
            obj.customer = request.user
            super().save_model(request, obj, form, change)


admin.site.register(Buyback, BuybackAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(SendList, SendListAdmin)
