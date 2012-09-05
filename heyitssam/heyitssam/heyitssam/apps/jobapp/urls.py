from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from models import *
from views import *
from django.views.generic import TemplateView, DetailView

urlpatterns = patterns('',
    url(r'^(?P<slug>.*)/contact/$', contact_view, name='contact'),
    url(r'^(?P<slug>.*)/resume/$', resume_view, name='resume'),
    url(r'^(?P<slug>.*)/cv/$', cv_view, name='cv'),
    url(r'^(?P<slug>.*)/$', overview, name='overview'),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template':'jobapp/index.html'}, name='index'),
)
