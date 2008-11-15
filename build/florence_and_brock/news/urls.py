from django.conf.urls.defaults import *


urlpatterns = patterns('news.views',
        url(r'^$', 'newsitem_list', name="newsitem_list"),
        url(r'^archive/$', 'newsitem_archive', name="newsitem_archive"),
        url('^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[\w-]+)/$', 'detail',
            name="newsitem_detail"),
        )

