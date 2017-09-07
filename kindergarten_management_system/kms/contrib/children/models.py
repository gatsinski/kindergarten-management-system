from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.utils.functional import cached_property

from kms.contrib.kindergartens.models import \
    Kindergarten
from kms.contrib.parents.models import \
    Parent


class Child(models.Model):
    first_name = models.CharField(_('First name'), max_length=254)
    middle_name = models.CharField(_('Middle name'), max_length=254)
    last_name = models.CharField(_('Last name'), max_length=254)
    birthdate = models.DateField(_('Birthdate'))
    personal_id = models.BigIntegerField(_('Personal ID'))
    parents = models.ManyToManyField(Parent)
    kindergarten = models.ForeignKey(Kindergarten)
    address = models.CharField(_('Address'), max_length=254)
    # Is the child currently enrolled in the kindergarten or its
    # application documents are still waiting to be approved by staff member
    is_active = models.BooleanField(_('Is active'), default=False)

    class Meta:
        verbose_name = _('Child')
        verbose_name_plural = _('Children')

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

    @property
    def age(self):
        return timezone.now().year - child.birthdate.year
