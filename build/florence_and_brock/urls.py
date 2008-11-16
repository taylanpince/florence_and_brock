from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.home', name="home"),
    url(r'^news/', include('news.urls')),
    url(r'^decisions/', include('decisions.urls')),
    url(r'^admin/(.*)', admin.site.root),

    url(r'^login/$', 'news.views.home_login', name="home_login"),
    url(r'^logout/$', 'news.views.home_logout', name="home_logout"),
)
