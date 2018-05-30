from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from .models import User, School, UserGroup


class UserResource(ModelResource):
    class Meta:
        model = User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = (
        'get_full_name',
        'email',
        'nationality',
        'school',
        'gender',
    )
    list_filter = (
        'gender',
        'nationality',
        'school',
    )
    resource_class = UserResource


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
    )
    list_filter = (
        'country',
    )


admin.site.unregister(Group)
admin.site.register(UserGroup)
