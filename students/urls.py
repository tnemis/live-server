from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from students.base_views import barcode_generator
from students.views.child_detail_views import *
urlpatterns = patterns('',
    url(
        regex=r'^id_card/?(?P<uid>\d+?)?/$',
        view=barcode_generator,
        name='students_barcode_generator'
    ),
    url(
        regex=r'^class_sectionwiseView/(?P<cl_id>\d+?)/$',
        view=login_required(class_sectionwiseView.as_view()),
        name='class_sectionwiseView'
    ),
    
    url(
        regex=r'^Child_detail_Sectionwise_detail/(?P<cl_id>\d+?)/(?P<sec_id>\w+?)/$',
        view=login_required(Child_detail_Sectionwise_detail.as_view()),
        name='Child_detail_Sectionwise_detail'
    ),


    url(
        regex=r'^child_admit/(?P<pk>\d+?)/$',
        view=login_required(Child_admit.as_view()),
        name='students_child_admit'
    ),

    url(
        regex=r'^child_detail/archive/$',
        view=login_required(Child_detailArchiveIndexView.as_view()),
        name='students_child_detail_archive_index'
    ),
    url(
        regex=r'^child_detail/create/$',
        view=login_required(Child_detailCreateView.as_view()),
        name='students_child_detail_create'
    ),
    url(
        regex=r'^child_detail/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=login_required(Child_detailDateDetailView.as_view()),
        name='students_child_detail_date_detail'
    ),
    url(
        regex=r'^child_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=login_required(Child_detailDayArchiveView.as_view()),
        name='students_child_detail_day_archive'
    ),
    url(
        regex=r'^child_detail/(?P<pk>\d+?)/delete/$',
        view=login_required(Child_detailDeleteView.as_view()),
        name='students_child_detail_delete'
    ),
    url(
        regex=r'^child_detail/(?P<pk>\d+?)/$',
        view=login_required(Child_detailDetailView.as_view()),
        name='Child_detailDetailView'
    ),
    url(
        regex=r'^child_detail_classwise/(?P<cl_id>\d+?)/$',
        view=login_required(Child_detailClasswiseView.as_view()),
        name='students_child_classwise_detail'
    ),

    # url(
    #     regex=r'^child_detail_classwiselist/(?P<cl_id>\d+?)/(?P<school_code>\d+?)/$',
    #     view=login_required(Child_detailClasswiseListView.as_view()),
    #     name='students_child_classwiselist_detail'
    # ),
    url(
        regex=r'^child_detail/$',
        view=login_required(Child_detailListView.as_view()),
        name='students_child_detail_list'
    ),
    url(
        regex=r'^Child_detailSectionListView/$',
        view=login_required(Child_detailSectionListView.as_view()),
        name='students_child_detail_section_list'
    ),

    url(
        regex=r'^child_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=login_required(Child_detailMonthArchiveView.as_view()),
        name='students_child_detail_month_archive'
    ),
    url(
        regex=r'^child_detail/today/$',
        view=login_required(Child_detailTodayArchiveView.as_view()),
        name='students_child_detail_today_archive'
    ),
    url(
        regex=r'^child_detail/(?P<pk>\d+?)/update/$',
        view=login_required(Child_detailUpdateView.as_view()),
        name='students_child_detail_update'
    ),
    url(
        regex=r'^child_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=login_required(Child_detailWeekArchiveView.as_view()),
        name='students_child_detail_week_archive'
    ),
    url(
        regex=r'^child_detail/archive/(?P<year>\d{4})/$',
        view=login_required(Child_detailYearArchiveView.as_view()),
        name='students_child_detail_year_archive'
    ),
    url(
        regex=r'^child_detail/transfer_detail/(?P<pk>\d+?)/$',
        view=login_required(Child_detailTransferView.as_view()),
        name='students_child_detail_transfer_detail'
    ),
    url(
        regex=r'^child_detail/pool_detail$',
        view=login_required(Child_detailPoolView.as_view()),
        name='students_child_detail_pool_detail'
    ),
    url(
        regex=r'^child_detail/pool_update/(?P<pk>\d+?)/$',
        view=login_required(Child_detailPoolUpdateView.as_view()),
        name='students_child_detail_pool_update'
    ),
    url(
        regex=r'^child_detail/download_child_profile/(?P<pk>\d+?)/$',
        view=login_required(Child_detailDownloadProfileView.as_view()),
        name='students_child_detail_download_profile'
    ),
    url(
        regex=r'^child_detail/child_pdfview/(?P<pk>\d+?)/$',
        view=login_required(child_pdfview.as_view()),
        name='students_child_detail_child_pdfview'
    ),
    url(  
        regex=r'^classwise_pdfview/(?P<pk>\d+?)/$',
        view=login_required(classwise_pdfview.as_view()),
        name='classwise_pdfview'
    ),
    
)


from students.views.child_family_detail_views import *
urlpatterns += patterns('',
    url(
        regex=r'^child_family_detail/archive/$',
        view=login_required(Child_family_detailArchiveIndexView.as_view()),
        name='students_child_family_detail_archive_index'
    ),
    url(
        regex=r'^child_family_detail/create/$',
        view=login_required(Child_family_detailCreateView.as_view()),
        name='students_child_family_detail_create'
    ),
    url(
        regex=r'^child_family_detail/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=login_required(Child_family_detailDateDetailView.as_view()),
        name='students_child_family_detail_date_detail'
    ),
    url(
        regex=r'^child_family_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=login_required(Child_family_detailDayArchiveView.as_view()),
        name='students_child_family_detail_day_archive'
    ),
    url(
        regex=r'^child_family_detail/(?P<pk>\d+?)/delete/$',
        view=login_required(Child_family_detailDeleteView.as_view()),
        name='students_child_family_detail_delete'
    ),
    url(
        regex=r'^child_family_detail/(?P<pk>\d+?)/$',
        view=login_required(Child_family_detailDetailView.as_view()),
        name='students_child_family_detail_detail'
    ),
    url(
        regex=r'^child_family_detail/$',
        view=login_required(Child_family_detailListView.as_view()),
        name='students_child_family_detail_list'
    ),
    url(
        regex=r'^child_family_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=login_required(Child_family_detailMonthArchiveView.as_view()),
        name='students_child_family_detail_month_archive'
    ),
    url(
        regex=r'^child_family_detail/today/$',
        view=login_required(Child_family_detailTodayArchiveView.as_view()),
        name='students_child_family_detail_today_archive'
    ),
    url(
        regex=r'^child_family_detail/(?P<pk>\d+?)/update/$',
        view=login_required(Child_family_detailUpdateView.as_view()),
        name='students_child_family_detail_update'
    ),
    url(
        regex=r'^child_family_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=login_required(Child_family_detailWeekArchiveView.as_view()),
        name='students_child_family_detail_week_archive'
    ),
    url(
        regex=r'^child_family_detail/archive/(?P<year>\d{4})/$',
        view=login_required(Child_family_detailYearArchiveView.as_view()),
        name='students_child_family_detail_year_archive'
    ),

)


from students.views.child_transfer_history_views import *
urlpatterns += patterns('',
    url(
        regex=r'^child_transfer_history/archive/$',
        view=login_required(Child_Transfer_HistoryArchiveIndexView.as_view()),
        name='students_child_transfer_history_archive_index'
    ),
    url(
        regex=r'^child_transfer_history/create/$',
        view=login_required(Child_Transfer_HistoryCreateView.as_view()),
        name='students_child_transfer_history_create'
    ),
    url(
        regex=r'^child_transfer_history/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=login_required(Child_Transfer_HistoryDateDetailView.as_view()),
        name='students_child_transfer_history_date_detail'
    ),
    url(
        regex=r'^child_transfer_history/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=login_required(Child_Transfer_HistoryDayArchiveView.as_view()),
        name='students_child_transfer_history_day_archive'
    ),
    url(
        regex=r'^child_transfer_history/(?P<pk>\d+?)/delete/$',
        view=login_required(Child_Transfer_HistoryDeleteView.as_view()),
        name='students_child_transfer_history_delete'
    ),
    url(
        regex=r'^child_transfer_history/(?P<pk>\d+?)/$',
        view=login_required(Child_Transfer_HistoryDetailView.as_view()),
        name='students_child_transfer_history_detail'
    ),
    url(
        regex=r'^child_transfer_history/$',
        view=login_required(Child_Transfer_HistoryListView.as_view()),
        name='students_child_transfer_history_list'
    ),
    url(
        regex=r'^child_transfer_history/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=login_required(Child_Transfer_HistoryMonthArchiveView.as_view()),
        name='students_child_transfer_history_month_archive'
    ),
    url(
        regex=r'^child_transfer_history/today/$',
        view=login_required(Child_Transfer_HistoryTodayArchiveView.as_view()),
        name='students_child_transfer_history_today_archive'
    ),
    url(
        regex=r'^child_transfer_history/(?P<pk>\d+?)/update/$',
        view=login_required(Child_Transfer_HistoryUpdateView.as_view()),
        name='students_child_transfer_history_update'
    ),
    url(
        regex=r'^child_transfer_history/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=login_required(Child_Transfer_HistoryWeekArchiveView.as_view()),
        name='students_child_transfer_history_week_archive'
    ),
    url(
        regex=r'^child_transfer_history/archive/(?P<year>\d{4})/$',
        view=login_required(Child_Transfer_HistoryYearArchiveView.as_view()),
        name='students_child_transfer_history_year_archive'
    ),
)


from students.views.block_views import *
urlpatterns += patterns('',
    url(
        regex=r'^block/$',
        view=login_required(BlockView.as_view()),
        name='block_detail'
    ),
)


from students.views.district_views import *
urlpatterns += patterns('',
    url(
        regex=r'^district/$',
        view=login_required(DistrictView.as_view()),
        name='district_detail'
    ),
)

from students.views.state_views import *
urlpatterns += patterns('',
    url(
        regex=r'^state/$',
        view=login_required(StateView.as_view()),
        name='state_detail'
    ),
)


from students.views.nominal_roll_reports import *
urlpatterns += patterns('',
    url(regex=r'^child_detail/nominal_roll_list/10/$',view=Nominal_roll_list_10.as_view(),name='nominal_roll_list_10'),
    url(regex=r'^child_detail/nominal_roll_list/11/$',view=Nominal_roll_list_11.as_view(),name='nominal_roll_list_11'),
    url(regex=r'^child_detail/nominal_roll_list/12/$',view=Nominal_roll_list_12.as_view(),name='nominal_roll_list_12'),
    url(regex=r'^child_detail/nominal_roll_checklist/(?P<pk>\d+?)/$',view=Nominal_roll_checklist.as_view(),name='nominal_roll_check_list'),
)
