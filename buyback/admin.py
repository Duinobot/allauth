from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Buyback, Exchange, BuybackItem, ExchangeItem, SendList

# Register your models here.


class BuybackAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Buyback


class ExchangeAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Exchange


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

    def save_model(self, request, obj, form, change):
        if obj.user is None:
            obj.user = request.user
        else:
            obj.user = form.user
        return super().save_model(request, obj, form, change)


admin.site.register(Buyback, BuybackAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(SendList, SendListAdmin)
