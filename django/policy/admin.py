from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Stage, Price, AccommodationOption, PaymentInfo


class PriceAdmin(admin.ModelAdmin):
    list_display = ('description', 'krw', 'usd')


class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'num_rooms', 'price_krw', 'price_usd')


admin.site.register(Price, PriceAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
admin.site.register(Stage, SingletonModelAdmin)
admin.site.register(PaymentInfo, SingletonModelAdmin)
