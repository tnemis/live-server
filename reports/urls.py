from django.conf.urls import patterns, url
from reports.views import *

urlpatterns = patterns('',
    url(
        regex=r'^list/$',
        view=ReportView.as_view(),
        name='report_list'
    ),
    url(r'^download_child_profile/(?P<ch_id>\d+)/$', download_child_profile),
)



