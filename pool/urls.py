from django.conf.urls import patterns, url
from students.base_views import barcode_generator
from students.views.child_detail_views import *
from students.views.child_family_detail_views import *
from students.views.child_transfer_history_views import *
from pool.views import *
from django.contrib.auth.decorators import login_required



urlpatterns = patterns('',
    
   
    url(
        regex=r'^block_report/(?P<pk>\d+?)/$',
        view=login_required(BlockPoolReport.as_view()),
        name='block_pool_report'
    ),
    url(
        regex=r'^district_report/(?P<pk>\d+?)/$',
        view=login_required(DistrictPoolReport.as_view()),
        name='district_pool_report'
    ),
    url(
        regex=r'^state_report/$',
        view=login_required(StatePoolReport.as_view()),
        name='state_pool_report'
    ),

    url(
        regex=r'^school_report/(?P<pk>\d+?)/$',
        view=login_required(SchoolPoolReport.as_view()),
        name='school_pool_report'
    ),


   

)
