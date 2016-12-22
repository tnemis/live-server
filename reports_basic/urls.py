from django.conf.urls import patterns, url
from reports_basic.views import *

urlpatterns = patterns('',
    url(
        regex=r'^list_basic/$',
        view=ReportViewBasic.as_view(),
        name='report_list_basic'
    ),
    url(r'^download_child_profile/(?P<ch_id>\d+)/$', download_child_profile),
)



