from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^news/', include('news.urls')),
    (r'^admin/(.*)', admin.site.root),

    # Temporary Base Template
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
)
