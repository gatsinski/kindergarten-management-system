from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .urls import urlpatterns


@apphook_pool.register
class ApplicationApp(CMSApp):
    name = _("Application App")
    urls = [urlpatterns]
    app_name = "applications"
