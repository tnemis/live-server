from django.conf.urls import patterns, url
from students.base_views import barcode_generator
from students.views.child_detail_views import *
from students.views.child_family_detail_views import *
from students.views.child_transfer_history_views import *
from bus_pass.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    
    url(
        regex=r'^school_report/(?P<pk>\d+?)/$',
        view=login_required(SchoolBusPassReport.as_view()),
        name='school_bus_pass_report'
    ),
    url(
        regex=r'^block_report/(?P<pk>\d+?)/$',
        view=login_required(BlockBusPassReport.as_view()),
        name='block_bus_pass_report'
    ),
    url(
        regex=r'^district_report/(?P<pk>\d+?)/$',
        view=login_required(DistrictBusPassReport.as_view()),
        name='district_bus_pass_report'
    ),
    url(
        regex=r'^state_report/$',
        view=login_required(StateBusPassReport.as_view()),
        name='state_bus_pass_report'
    ),
    url(
        regex=r'^list/(?P<school>\d+?)/(?P<cls>\d+?)/$',
        view=Name_list.as_view(),
        name='bus_pass_name_list'
    ),
    url(
        regex=r'^list_all/(?P<school>\d+?)/$',
        view=Name_list_all.as_view(),
        name='bus_pass_name_list_all'
    ),

)
