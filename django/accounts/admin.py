from django.contrib import admin

from .models import User, School


class UserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'email', 'nationality', 'school', 'gender')
    list_filter = ('gender', 'nationality', 'school')


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)


admin.site.register(User, UserAdmin)
admin.site.register(School, SchoolAdmin)
