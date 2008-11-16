from django.conf.urls.defaults import *

urlpatterns = patterns('residents.views',
    url(r'^$', 'contact_list', name="residents_contact_list"),
)
