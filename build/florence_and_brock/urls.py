from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name="home"),
    url(r'^news/', include('news.urls')),
    url(r'^decisions/', include('decisions.urls')),
    url(r'^contacts/', include('residents.urls')),
    url(r'^admin/(.*)', admin.site.root),

    url(r'^account/$', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    url(r'^account/', include('django.contrib.auth.urls')),
)
