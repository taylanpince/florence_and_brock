from django.contrib import admin
from django.conf.urls.defaults import *


admin.autodiscover()


home_dict = {
    'cat_slug': 'featured',
    'num_per_page': 6,
}

urlpatterns = patterns('',

    # Admin
    (r'^admin/(.*)', admin.site.root),

    # Temporary Base Template
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
)
