from django.contrib import admin

from kindergarten_management_system.contrib.kindergartens.models import \
    Kindergarten, KindergartenType, City


@admin.register(Kindergarten)
class KindergartenAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'city')


@admin.register(KindergartenType)
class KindergartenTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
