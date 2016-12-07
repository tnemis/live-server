from django.conf.urls import patterns, url
from udise.reports import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(regex=r'^state_level_udise_report/$',view=login_required(State_level_udise_report.as_view()),name='state_level_udise_report'),
    url(regex=r'^block_level_udise_report/(?P<pk>\d+?)/$',view=login_required(Block_level_udise_report.as_view()),name='block_level_udise_report'),
    url(regex=r'^district_level_udise_report/(?P<pk>\d+?)/$',view=login_required(District_level_udise_report.as_view()),name='district_level_udise_report'),
    url(regex=r'^school_level_udise_report/(?P<pk>\d+?)/$',view=login_required(School_level_udise_report.as_view()),name='school_level_udise_report'),
)
