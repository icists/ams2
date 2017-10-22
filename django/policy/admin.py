from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Stage, Price, AccommodationOption, PaymentInfo, Room


class PriceAdmin(admin.ModelAdmin):
    list_display = ('description', 'price_krw', 'price_usd')


class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = ('description', 'capacity', 'num_rooms', 'price_krw', 'price_usd')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'occupied_seats', 'full_capacity')


admin.site.register(Price, PriceAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
admin.site.register(Stage, SingletonModelAdmin)
admin.site.register(PaymentInfo, SingletonModelAdmin)
admin.site.register(Room, RoomAdmin)
