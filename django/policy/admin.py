from django.contrib import admin

from .models import Stage, Price, AccommodationOption, PaymentInfo


class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('description', 'krw', 'usd')


class AccommodationOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'num_rooms', 'price_krw', 'price_usd')


class PaymentInfoAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'bank_name', 'bank_branch', 'account_number', 'swift_code')

    def has_add_permission(self, request):
        # Allow at most one payment info
        num_objects = self.model.objects.count()
        return num_objects < 1


admin.site.register(Price, PriceAdmin)
admin.site.register(AccommodationOption, AccommodationOptionAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(PaymentInfo, PaymentInfoAdmin)
