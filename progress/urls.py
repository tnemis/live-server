from django.conf.urls import patterns, url
from progress.reports import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(regex=r'^state_level_progress_report/$',
    	view=login_required(State_level_progress_report.as_view()),
    	name='state_level_progress_report'),
    url(regex=r'^state_level_progress_report_man_dee/8/$',
    	view=login_required(State_level_progress_report_man_dee1.as_view()),
    	name='state_level_progress_report_dee'),
    url(regex=r'^block_level_progress_report/(?P<pk>\d+?)/$',
    	view=login_required(Block_level_progress_report.as_view()),
    	name='block_level_progress_report'),
    url(regex=r'^district_level_progress_report/(?P<pk>\d+?)/$',
    	view=login_required(District_level_progress_report.as_view()),
    	name='district_level_progress_report'),
    url(regex=r'^school_level_progress_report/(?P<pk>\d+?)/$',
    	view=login_required(School_level_progress_report.as_view()),
    	name='school_level_progress_report'),
    url(regex=r'^district_dse_progress_report/(?P<pk>\d+?)/$',
    	view=login_required(District_dse_progress_report.as_view()),
    	name='district_dse_progress_report'),
    url(regex=r'^district_matric_progress_report/(?P<pk>\d+?)/$',
    	view=login_required(District_matric_progress_report.as_view()),
    	name='district_matric_progress_report'),
)
