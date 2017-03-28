from django.db import models
from django.utils.translation import ugettext as _
from django.utils.functional import cached_property
from django.contrib.auth.models import User


class Parent(User):
    middle_name = models.CharField(_('Middle name'), max_length=254)
    address = models.CharField(_('Address'), max_length=254)
    telephone = models.CharField('Телефон', max_length=15)

    class Meta:
        verbose_name = _('Parent')
        verbose_name_plural = _('Parents')

    def __str__(self):
        return self.full_name

    @cached_property
    def full_name(self):
        return '{} {} {}'.format(self.first_name,
                                 self.middle_name,
                                 self.last_name)

    @cached_property
    def short_name(self):
        return '{} {}'.format(self.first_name,
                              self.last_name)
