from django.conf.urls import patterns, url
from reports.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

   url(
        regex=r'^aadhaar_report/$',
        view=aadhaar_report.as_view(),
        name='aadhaar_report'
    ),
    
    url(regex=r'^state_level_aadhaar_report/$',
        view=login_required(state_level_aadhaar_report.as_view()),
        name='state_level_aadhaar_report'),
    url(regex=r'^state_level_aadhaar_report_dee/$',
        view=login_required(state_level_aadhaar_report_dee.as_view()),
        name='state_level_aadhaar_report_dee'),
# District Login

    url(regex=r'^district_level_aadhaar_report/$',
        view=login_required(district_level_aadhaar_report.as_view()),
        name='district_level_aadhaar_report'),

    
    url(regex=r'^block_level_aadhaar_report/$',
        view=login_required(block_level_aadhaar_report.as_view()),
        name='block_level_aadhaar_report'),
    
# Matric
    url(
        regex=r'^state_level_aadhaar_report/matric_view/$',
        view=login_required(matric_view.as_view()),
        name='matric_view'),
    url(regex=r'^district_level_matric_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(District_level_matric_aadhaar_report.as_view()),
        name='district_level_matric_aadhaar_report'),
    url(regex=r'^block_level_matric_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(Block_level_matric_aadhaar_report.as_view()),
        name='block_level_matric_aadhaar_report'),
    url(regex=r'^school_matric_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(School_matric_aadhaar_report.as_view()),
        name='school_matric_aadhaar_report'),
# DEE Govt 
    url(regex=r'^state_level_aadhaar_report/dee_govt_view/$',
        view=login_required(dee_govt_view.as_view()),
        name='dee_govt_view'),
    url(regex=r'^state_level_aadhaar_report_dee/dee_govt_view/$',
        view=login_required(dee_govt_view.as_view()),
        name='dee_govt_view'),
    url(regex=r'^dee_govt_Dist_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_govt_Dist_aadhaar_report.as_view()),
        name='dee_govt_Dist_aadhaar_report'),
    url(regex=r'^dee_govt_block_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_govt_block_aadhaar_report.as_view()),
        name='dee_govt_block_aadhaar_report'),

    url(regex=r'^dee_govt_school_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_govt_school_aadhaar_report.as_view()),
        name='dee_govt_school_aadhaar_report'),
  # DEE Pvt Aided
    url(regex=r'^state_level_aadhaar_report/dee_pvt_aid_view/$',
        view=login_required(dee_pvt_aid_view.as_view()),
        name='dee_pvt_aid_view'),
    url(regex=r'^state_level_aadhaar_report_dee/dee_pvt_aid_view/$',
        view=login_required(dee_pvt_aid_view.as_view()),
        name='dee_pvt_aid_view'),
    url(regex=r'^dee_pvt_aided_Dist_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_pvt_aided_Dist_aadhaar_report.as_view()),
        name='dee_pvt_aided_Dist_aadhaar_report'),
    url(regex=r'^dee_pvt_aided_block_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_pvt_aided_block_aadhaar_report.as_view()),
        name='dee_pvt_aided_block_aadhaar_report'),
    url(regex=r'^dee_pvt_aided_school_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_pvt_aided_school_aadhaar_report.as_view()),
        name='dee_pvt_aided_school_aadhaar_report'),
#DEE Pvt Unaided
    url(regex=r'^state_level_aadhaar_report/dee_pvt_unaid_view/$',
        view=login_required(dee_pvt_unaid_view.as_view()),
        name='dee_pvt_unaid_view'),
    url(regex=r'^state_level_aadhaar_report_dee/dee_pvt_unaid_view/$',
        view=login_required(dee_pvt_unaid_view.as_view()),
        name='dee_pvt_unaid_view'),
    url(regex=r'^dee_pvt_unaided_Dist_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_pvt_unaided_Dist_aadhaar_report.as_view()),
        name='dee_pvt_unaided_Dist_aadhaar_report'),
    url(regex=r'^dee_pvt_unaided_block_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_pvt_unaided_block_aadhaar_report.as_view()),
        name='dee_pvt_unaided_block_aadhaar_report'),
    url(regex=r'^dee_pvt_unaided_school_aadhaar_report/(?P<pk>\d+?)/$',
        view=login_required(dee_pvt_unaided_school_aadhaar_report.as_view()),
        name='dee_pvt_unaided_school_aadhaar_report'),

#dse district
     url(
        regex=r'^state_level_aadhaar_report/dse_govt_view/$',
        view=login_required(dse_govt_view.as_view()),
        name='dse_govt_view'),
      url(
        regex=r'^state_level_aadhaar_report/dse_pvt_a_view/$',
        view=login_required(dse_pvt_a_view.as_view()),
        name='dse_pvt_a_view'),
       url(
        regex=r'^state_level_aadhaar_report/dse_pvt_ua_view/$',
        view=login_required(dse_pvt_ua_view.as_view()),
        name='dse_pvt_ua_view'),
        url(
        regex=r'^state_level_aadhaar_report/cbse_icse_view/$',
        view=login_required(cbse_icse_view.as_view()),
        name='cbse_icse_view'),

#dse block
 
    url(regex=r'^d_l_dse_g_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(d_l_dse_g_aadhaar.as_view()),
        name='d_l_dse_g_aadhaar'),

    url(regex=r'^d_l_dse_a_addhaar/(?P<pk>\d+?)/$',
        view=login_required(d_l_dse_a_addhaar.as_view()),
        name='d_l_dse_a_addhaar'),
 
    url(regex=r'^d_l_dse_ua_addhaar/(?P<pk>\d+?)/$',
        view=login_required(d_l_dse_ua_addhaar.as_view()),
        name='d_l_dse_ua_addhaar'),
 
    url(regex=r'^d_l_cbse_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(d_l_cbse_aadhaar.as_view()),
        name='district_level_matric_ad_l_cbse_aadhaaradhaar_report'),

# dse block-schoolwise

    url(regex=r'^b_l_dse_g_aadhar/(?P<pk>\d+?)/$',
        view=login_required(b_l_dse_g_aadhar.as_view()),
        name='b_l_dse_g_aadhar'),
    url(regex=r'^b_l_dse_a_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(b_l_dse_a_aadhaar.as_view()),
        name='b_l_dse_a_aadhaar'),
    url(regex=r'^b_l_dse_ua_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(b_l_dse_ua_aadhaar.as_view()),
        name='b_l_dse_ua_aadhaar'),
    url(regex=r'^b_l_cbse/(?P<pk>\d+?)/$',
        view=login_required(b_l_cbse.as_view()),
        name='b_l_cbse'),

# dse schoolwise 

    url(regex=r'^s_l_dse_govt_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(s_l_dse_govt_aadhaar.as_view()),
        name='s_l_dse_govt_aadhaar'),
    url(regex=r'^s_l_dse_a_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(s_l_dse_a_aadhaar.as_view()),
        name='s_l_dse_a_aadhaar'),
    url(regex=r'^s_l_dse_ua_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(s_l_dse_ua_aadhaar.as_view()),
        name='s_l_dse_ua_aadhaar'),
    url(regex=r'^s_l_cbse_aadhaar/(?P<pk>\d+?)/$',
        view=login_required(s_l_cbse_aadhaar.as_view()),
        name='s_l_cbse_aadhaar'),


)

