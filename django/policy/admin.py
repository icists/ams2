from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Stage, Price, AccommodationOption, PaymentInfo, Room, Configuration, EssayTopic, ProjectTopic


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'price_krw',
        'price_usd',
    )


@admin.register(AccommodationOption)
class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'capacity',
        'num_rooms',
        'price_krw',
        'price_usd',
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'occupied_seats',
        'full_capacity',
    )


@admin.register(EssayTopic)
class EssayTopicAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )


@admin.register(ProjectTopic)
class ProjectTopicAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )


admin.site.register(Stage, SingletonModelAdmin)
admin.site.register(PaymentInfo, SingletonModelAdmin)
admin.site.register(Configuration, SingletonModelAdmin)
