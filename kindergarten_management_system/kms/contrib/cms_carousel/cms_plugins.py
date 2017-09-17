from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import CarouselContainerPluginModel, CarouselImagePluginModel


class CarouselContainerPluginPublisher(CMSPluginBase):
    model = CarouselContainerPluginModel
    module = _('Carousel')
    name = _('Carousel container')
    allow_children = True
    child_classes = ('CarouselImagePluginPublisher')
    prepopulated_fields = {'slug': ('title',)}
    render_template = 'carousels/container.html'


class CarouselImagePluginPublisher(CMSPluginBase):
    model = CarouselImagePluginModel
    module = _('Carousel')
    name = _('Image')
    require_parent = True
    parent_classes = ('CarouselContainerPluginPublicher',)
    render_template = 'carousels/image.html'


plugin_pool.register_plugin(CarouselContainerPluginPublisher)
plugin_pool.register_plugin(CarouselImagePluginPublisher)
