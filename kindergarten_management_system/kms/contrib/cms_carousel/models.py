from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property

from cms.models import CMSPlugin

from filer.fields.image import FilerImageField


class CarouselContainerPluginModel(CMSPlugin):
    title = models.CharField(_('Title'), max_length=254)
    slug = models.SlugField(_('Slug'), max_length=254)

    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')

    def __str__(self):
        return self.title

    @cached_property
    def pretty_id(self):
        # Used in HTML templates
        return '{}-{}'.format(self.slug, self.pk)


class CarouselImagePluginModel(CMSPlugin):
    title = models.CharField(_('Text'), max_length=254, blank=True)
    text = models.TextField(_('Text'), max_length=1000, blank=True)
    image = FilerImageField(verbose_name=_('Image'),
                            related_name='carousel_images',
                            on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Carousel image')
        verbose_name_plural = _('Carousel images')

    def __str__(self):
        return 'Carousel image {}'.format(self.pk)
