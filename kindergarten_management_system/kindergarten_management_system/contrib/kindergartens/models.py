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


class GroupType(models.Model):
    name = models.CharField(_('Name'), max_length=254)

    class Meta:
        verbose_name = _('Group type')
        verbose_name_plural = _('Group types')

    def __str__(self):
        return '{}'.format(self.name)


class Group(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    type = models.ForeignKey(GroupType)
    kindergarten = models.ForeignKey(Kindergarten)
    description = models.CharField(_('Description'), max_length=1000)

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    def __str__(self):
        return '{}, {}'.format(self.name, self.kindergarten)
