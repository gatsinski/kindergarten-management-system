from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.utils.functional import cached_property

from kindergarten_management_system.contrib.kindergartens.models import \
    Kindergarten
from kindergarten_management_system.contrib.parents.models import Parent
from kindergarten_management_system.contrib.children.models import Child


class Application(models.Model):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    PENDING = 'pending'

    STATUS_CHOICES = (
        (APPROVED, _('Approved')),
        (REJECTED, _('Rejected')),
        (PENDING, _('Pending')),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    kindergarten = models.ForeignKey(Kindergarten)
    parent = models.ForeignKey(Parent)
    child = models.ForeignKey(Child)
    status = models.CharField(_('Status'),
                              max_length=254,
                              choices=STATUS_CHOICES,
                              default=PENDING)

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

    def __str__(self):
        return '{}'.format(self.reference_number)

    @cached_property
    def reference_number(self):
        return '{}/{}'.format(self.date_created.strftime('%d.%m.%Y'), self.pk)


class Attachment(models.Model):
    # Might be raplaced with GenericForeignKey in the future
    # in order to be used by all django applications
    application = models.ForeignKey(Application)
    name = models.CharField(_('Name'), max_length=254)
    file = models.FileField(upload_to='attachments')
