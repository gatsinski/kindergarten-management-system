from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from cms.models import CMSPlugin


class ContentBlockPluginModel(CMSPlugin):
    CADET_BLUE = 'cadet_blue'
    BURLYWOOD = 'burlywood'
    AZURE = 'azure'
    ALICE_BLUE = 'alice_blue'
    CORN_SILK = 'corn_silk'

    STATUS_CHOICES = (
        (CADET_BLUE, _('Cadet blue')),
        (BURLYWOOD, _('Burlywood')),
        (AZURE, _('Azure')),
        (ALICE_BLUE, _('Alize blue')),
        (CORN_SILK, _('Corn silk')),
    )

    title = models.CharField(_('Title'), max_length=254)
    slug = models.SlugField(_('Slug'), max_length=254)
    type = models.CharField(_('Block type'),
                            max_length=254,
                            choices=STATUS_CHOICES,
                            default=CADET_BLUE)

    class Meta:
        verbose_name = _('Content blok')
        verbose_name_plural = _('Content blocks')

    def __str__(self):
        return self.title

    @cached_property
    def pretty_id(self):
        # Used in HTML templates
        return '{}-{}'.format(self.slug, self.pk)

    @cached_property
    def color_class(self):
        return self.type.replace('_', '-')
