from django.conf.urls.defaults import *

urlpatterns = patterns('pagination.tests.views',
    url(r'^list/$', 'testmodel_list', name='pagination_testmodel_list'),
        )
