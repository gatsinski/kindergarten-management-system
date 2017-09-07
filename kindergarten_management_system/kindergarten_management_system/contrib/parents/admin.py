from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ExportMixin

from .models import Parent


class ParentResource(ModelResource):

    class Meta:
        model = Parent
        fields = ('username',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'address',
                  'telephone',)


@admin.register(Parent)
class ParentAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name')
    resource_class = ParentResource
