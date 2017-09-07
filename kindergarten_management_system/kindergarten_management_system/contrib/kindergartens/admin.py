from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin, ExportMixin

from .models import Kindergarten, KindergartenType, City


class KindergartenResource(ModelResource):

    class Meta:
        model = Kindergarten
        fields = ('name',
                  'type',
                  'city')

    def dehydrate_type(self, kindergarten):
        return kindergarten.type.name

    def dehydrate_city(self, kindergarten):
        return kindergarten.city.name


@admin.register(Kindergarten)
class KindergartenAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'type', 'city')
    resource_class = KindergartenResource


@admin.register(KindergartenType)
class KindergartenTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    pass
