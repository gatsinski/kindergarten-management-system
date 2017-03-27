from django.contrib import admin

from kindergarten_management_system.contrib.teachers.models import \
    Teacher, Specialty


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'middle_name',
                    'last_name',
                    'specialty',
                    'kindergarten')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass
