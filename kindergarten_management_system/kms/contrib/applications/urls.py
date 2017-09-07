from django.conf.urls import url

from .views import ApplicationWizard

urlpatterns = [
    url(r'^$', ApplicationWizard.as_view(), name='create_application'),
]
