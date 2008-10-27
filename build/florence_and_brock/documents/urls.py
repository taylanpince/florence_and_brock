from django.conf.urls.defaults import *


urlpatterns = patterns('documents.views',
    url(r'^$', 'document_list', name='document_list'),
)
