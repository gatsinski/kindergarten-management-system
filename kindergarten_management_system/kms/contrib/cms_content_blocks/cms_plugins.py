from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ContentBlockPluginModel


class ContentBlockPluginPublisher(CMSPluginBase):
    model = ContentBlockPluginModel
    module = _('Blocks')
    name = _('Content block')
    allow_children = True
    prepopulated_fields = {'slug': ('title',)}
    render_template = 'cms_content_blocks/block.html'


plugin_pool.register_plugin(ContentBlockPluginPublisher)
