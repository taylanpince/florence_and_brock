from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name="home"),
    url(r'^news/', include('news.urls')),
    url(r'^decisions/', include('decisions.urls')),
    url(r'^contacts/', include('residents.urls')),
    url(r'^admin/(.*)', admin.site.root),

    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
)
