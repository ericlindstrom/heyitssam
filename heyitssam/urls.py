from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from apps.jobapp.models import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template':'robots.txt', 'mimetype':'text/plain'},),
    url(r'^', include('apps.jobapp.urls', namespace='jobapp')),
    #url(r'^heyitssam/', include('heyitssam.foo.urls')),
)

print settings.STATIC_ROOT

if settings.DEBUG:
    urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	    'document_root': settings.MEDIA_ROOT,
	}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
	    'document_root': settings.STATIC_ROOT,
	}),

   )
