from django.contrib import admin
from django.utils.translation import ugettext as _

from parler.admin import TranslatableAdmin, TranslatableTabularInline

from .models import Application, Attachment, Test, TestInline


class AttachmentInline(admin.TabularInline):
    model = Attachment
    verbose_name = _('Attachment')
    verbose_name_plural = _('Attachments')
    readonly_fields = ('name', 'file')
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('date_created',
                    'kindergarten',
                    'status')
    readonly_fields = ('date_created',
                       'date_modified',
                       'kindergarten',
                       'parent',
                       'child')
    inlines = [AttachmentInline]


class TestAdminInline(TranslatableTabularInline):
    model = TestInline
    fields = ('name',)


@admin.register(Test)
class TestAdmin(TranslatableAdmin):
    inlines = (TestAdminInline,)
    pass
