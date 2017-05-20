from django.contrib import admin

from import_export import fields
from import_export.admin import ExportMixin
from import_export.resources import ModelResource

from kindergarten_management_system.contrib.teachers.models import \
    Teacher, Specialty


class TeacherResource(ModelResource):
    city = fields.Field(column_name='city')

    class Meta:
        model = Teacher
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'specialty',
                  'kindergarten')
        export_order = ('first_name',
                        'middle_name',
                        'last_name',
                        'specialty',
                        'kindergarten',
                        'city')

    def dehydrate_specialty(self, teacher):
        return teacher.specialty.name

    def dehydrate_kindergarten(self, teacher):
        return teacher.kindergarten.name

    def dehydrate_city(self, teacher):
        return teacher.kindergarten.city.name


@admin.register(Teacher)
class TeacherAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name',
                    'specialty',
                    'kindergarten')
    resource_class = TeacherResource


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass
