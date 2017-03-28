from django.contrib import admin

from kindergarten_management_system.contrib.parents.models import \
    Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name')
