from django.contrib import admin

from kindergarten_management_system.contrib.children.models import \
    Child


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name',
                    'birthdate',
                    'is_active')
    date_hierarchy = 'birthdate'
