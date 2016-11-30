from django.conf.urls import include, url

from .views import TemplatesView

urlpatterns = (
    url(r'$', TemplatesView.as_view(), name='templates'),
)