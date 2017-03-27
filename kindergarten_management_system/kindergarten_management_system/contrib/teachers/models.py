from django.db import models
from django.utils.translation import ugettext as _
from django.utils.functional import cached_property
from django.contrib.auth.models import User

from kindergarten_management_system.contrib.kindergartens.models import \
    Kindergarten


class Specialty(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    description = models.CharField(_('Description'), max_length=1000)

    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')

    def __str__(self):
        return '{}'.format(self.name)


class Teacher(User):
    middle_name = models.CharField(_('Middle name'), max_length=254)
    specialty = models.ForeignKey(Specialty)
    kindergarten = models.ForeignKey(Kindergarten)
    address = models.CharField(_('Address'), max_length=254)
    telephone = models.CharField('Телефон', max_length=15)

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

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
