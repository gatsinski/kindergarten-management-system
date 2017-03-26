from django.db import models
from django.utils.translation import ugettext as _


class KindergartenType(models.Model):
    name = models.CharField(_('Name'), max_length=254)

    class Meta:
        verbose_name = _('Kindergarten type')
        verbose_name_plural = _('Kindergarten types')

    def __str__(self):
        return '{}'.format(self.name)


class City(models.Model):
    name = models.CharField(_('Name'), max_length=254)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return '{}'.format(self.name)


class Kindergarten(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    type = models.ForeignKey(KindergartenType)
    city = models.ForeignKey(City)
    address = models.CharField(_('Address'), max_length=254)

    class Meta:
        verbose_name = _('Kindergarten')
        verbose_name_plural = _('Kindergartens')

    def __str__(self):
        return '{}, {}'.format(self.name, self.city.name)
