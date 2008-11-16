from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name="home"),
    url(r'^news/', include('news.urls')),
    url(r'^decisions/', include('decisions.urls')),
    url(r'^admin/(.*)', admin.site.root),

    # Temporary Base Template
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
)
