from django.contrib import admin

from .models import Group, Application, Order


class GroupAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'size')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'stage', 'screening_result', 'group', 'group_discount',
                    'visa_letter', 'financial_aid', 'previous_participation')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'accommodation', 'breakfast_option', 'pre_option', 'post_option',
                    'paid_amount', 'total_cost', 'payment_status')


admin.site.register(Group, GroupAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Order, OrderAdmin)
