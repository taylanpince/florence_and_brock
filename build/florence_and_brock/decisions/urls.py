from django.conf.urls.defaults import *

urlpatterns = patterns('decisions.views',
    url(r'^issue/(?P<issue_id>\d+)/$', 'issue_vote', name="decisions_issue_vote"),
)
