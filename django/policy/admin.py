from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Stage, Price, AccommodationOption, PaymentInfo, Room, Configuration, EssayTopic, ProjectTopic


class PriceAdmin(admin.ModelAdmin):
    list_display = ('description', 'price_krw', 'price_usd')


class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = ('description', 'capacity', 'num_rooms', 'price_krw', 'price_usd')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'occupied_seats', 'full_capacity')


class EssayTopicAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class ProjectTopicAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


admin.site.register(Price, PriceAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
admin.site.register(Stage, SingletonModelAdmin)
admin.site.register(PaymentInfo, SingletonModelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Configuration, SingletonModelAdmin)
admin.site.register(EssayTopic, EssayTopicAdmin)
admin.site.register(ProjectTopic, ProjectTopicAdmin)
