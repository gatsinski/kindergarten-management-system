from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ExportMixin

from .models import Child


class ChildResource(ModelResource):

    class Meta:
        model = Child
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'personal_id',
                  'birthdate',
                  'kindergarten',
                  'address',
                  'parents',
                  'is_active')

    def dehydrate_birthdate(self, child):
        return child.birthdate.strftime('%d.%m.%Y')

    def dehydrate_kindergarten(self, child):
        return child.kindergarten.name

    def dehydrate_parents(self, child):
        parents = [parent.full_name for parent in child.parents.all()]
        return ', '.join(parents)


@admin.register(Child)
class ChildAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name',
                    'birthdate',
                    'is_active')
    date_hierarchy = 'birthdate'
    resource_class = ChildResource
