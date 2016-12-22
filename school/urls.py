from django.conf.urls import patterns, url



from school.views.crc_views import *
urlpatterns = patterns('',

    url(
        regex=r'^crc/create/$',
        view=CrcCreateView.as_view(),
        name='school_crc_create'
    ),


    url(
        regex=r'^crc/(?P<pk>\d+?)/delete/$',
        view=CrcDeleteView.as_view(),
        name='school_crc_delete'
    ),
    url(
        regex=r'^crc/(?P<pk>\d+?)/$',
        view=CrcDetailView.as_view(),
        name='school_crc_detail'
    ),
    url(
        regex=r'^crc/$',
        view=CrcListView.as_view(),
        name='school_crc_list'
    ),


    url(
        regex=r'^crc/(?P<pk>\d+?)/update/$',
        view=CrcUpdateView.as_view(),
        name='school_crc_update'
    ),


)


from school.views.brc_views import *
urlpatterns += patterns('',

    url(
        regex=r'^brc/create/$',
        view=BrcCreateView.as_view(),
        name='school_brc_create'
    ),


    url(
        regex=r'^brc/(?P<pk>\d+?)/delete/$',
        view=BrcDeleteView.as_view(),
        name='school_brc_delete'
    ),
    url(
        regex=r'^brc/(?P<pk>\d+?)/$',
        view=BrcDetailView.as_view(),
        name='school_brc_detail'
    ),
    url(
        regex=r'^brc/$',
        view=BrcListView.as_view(),
        name='school_brc_list'
    ),


    url(
        regex=r'^brc/(?P<pk>\d+?)/update/$',
        view=BrcUpdateView.as_view(),
        name='school_brc_update'
    ),


)


from school.views.area_classification_views import *
urlpatterns += patterns('',

    url(
        regex=r'^area_classification/create/$',
        view=Area_classificationCreateView.as_view(),
        name='school_area_classification_create'
    ),


    url(
        regex=r'^area_classification/(?P<pk>\d+?)/delete/$',
        view=Area_classificationDeleteView.as_view(),
        name='school_area_classification_delete'
    ),
    url(
        regex=r'^area_classification/(?P<pk>\d+?)/$',
        view=Area_classificationDetailView.as_view(),
        name='school_area_classification_detail'
    ),
    url(
        regex=r'^area_classification/$',
        view=Area_classificationListView.as_view(),
        name='school_area_classification_list'
    ),


    url(
        regex=r'^area_classification/(?P<pk>\d+?)/update/$',
        view=Area_classificationUpdateView.as_view(),
        name='school_area_classification_update'
    ),


)


from school.views.school_category_views import *
urlpatterns += patterns('',

    url(
        regex=r'^school_category/create/$',
        view=School_categoryCreateView.as_view(),
        name='school_school_category_create'
    ),


    url(
        regex=r'^school_category/(?P<pk>\d+?)/delete/$',
        view=School_categoryDeleteView.as_view(),
        name='school_school_category_delete'
    ),
    url(
        regex=r'^school_category/(?P<pk>\d+?)/$',
        view=School_categoryDetailView.as_view(),
        name='school_school_category_detail'
    ),
    url(
        regex=r'^school_category/$',
        view=School_categoryListView.as_view(),
        name='school_school_category_list'
    ),


    url(
        regex=r'^school_category/(?P<pk>\d+?)/update/$',
        view=School_categoryUpdateView.as_view(),
        name='school_school_category_update'
    ),


)


from school.views.school_type_views import *
urlpatterns += patterns('',

    url(
        regex=r'^school_type/create/$',
        view=School_typeCreateView.as_view(),
        name='school_school_type_create'
    ),


    url(
        regex=r'^school_type/(?P<pk>\d+?)/delete/$',
        view=School_typeDeleteView.as_view(),
        name='school_school_type_delete'
    ),
    url(
        regex=r'^school_type/(?P<pk>\d+?)/$',
        view=School_typeDetailView.as_view(),
        name='school_school_type_detail'
    ),
    url(
        regex=r'^school_type/$',
        view=School_typeListView.as_view(),
        name='school_school_type_list'
    ),


    url(
        regex=r'^school_type/(?P<pk>\d+?)/update/$',
        view=School_typeUpdateView.as_view(),
        name='school_school_type_update'
    ),


)


from school.views.school_managed_views import *
urlpatterns += patterns('',

    url(
        regex=r'^school_managed/create/$',
        view=School_managedCreateView.as_view(),
        name='school_school_managed_create'
    ),


    url(
        regex=r'^school_managed/(?P<pk>\d+?)/delete/$',
        view=School_managedDeleteView.as_view(),
        name='school_school_managed_delete'
    ),
    url(
        regex=r'^school_managed/(?P<pk>\d+?)/$',
        view=School_managedDetailView.as_view(),
        name='school_school_managed_detail'
    ),
    url(
        regex=r'^school_managed/$',
        view=School_managedListView.as_view(),
        name='school_school_managed_list'
    ),


    url(
        regex=r'^school_managed/(?P<pk>\d+?)/update/$',
        view=School_managedUpdateView.as_view(),
        name='school_school_managed_update'
    ),


)


from school.views.school_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school/archive/$',
        view=SchoolArchiveIndexView.as_view(),
        name='school_school_archive_index'
    ),
    url(
        regex=r'^school/create/$',
        view=SchoolCreateView.as_view(),
        name='school_school_create'
    ),
    url(
        regex=r'^school/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=SchoolDateDetailView.as_view(),
        name='school_school_date_detail'
    ),
    url(
        regex=r'^school/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=SchoolDayArchiveView.as_view(),
        name='school_school_day_archive'
    ),
    url(
        regex=r'^school/(?P<pk>\d+?)/delete/$',
        view=SchoolDeleteView.as_view(),
        name='school_school_delete'
    ),
    url(
        regex=r'^school/(?P<pk>\d+?)/$',
        view=SchoolDetailView.as_view(),
        name='school_school_detail'
    ),
    url(
        regex=r'^school/$',
        view=SchoolListView.as_view(),
        name='school_school_list'
    ),
    url(
        regex=r'^school/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=SchoolMonthArchiveView.as_view(),
        name='school_school_month_archive'
    ),
    url(
        regex=r'^school/today/$',
        view=SchoolTodayArchiveView.as_view(),
        name='school_school_today_archive'
    ),
    url(
        regex=r'^school/(?P<pk>\d+?)/update/$',
        view=SchoolUpdateView.as_view(),
        name='school_school_update'
    ),
    url(
        regex=r'^school/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=SchoolWeekArchiveView.as_view(),
        name='school_school_week_archive'
    ),
    url(
        regex=r'^school/archive/(?P<year>\d{4})/$',
        view=SchoolYearArchiveView.as_view(),
        name='school_school_year_archive'
    ),
)


from school.views.school_contact_detail_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_contact_detail/archive/$',
        view=School_contact_detailArchiveIndexView.as_view(),
        name='school_school_contact_detail_archive_index'
    ),
    url(
        regex=r'^school_contact_detail/create/$',
        view=School_contact_detailCreateView.as_view(),
        name='school_school_contact_detail_create'
    ),
    url(
        regex=r'^school_contact_detail/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_contact_detailDateDetailView.as_view(),
        name='school_school_contact_detail_date_detail'
    ),
    url(
        regex=r'^school_contact_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_contact_detailDayArchiveView.as_view(),
        name='school_school_contact_detail_day_archive'
    ),
    url(
        regex=r'^school_contact_detail/(?P<pk>\d+?)/delete/$',
        view=School_contact_detailDeleteView.as_view(),
        name='school_school_contact_detail_delete'
    ),
    url(
        regex=r'^school_contact_detail/(?P<pk>\d+?)/$',
        view=School_contact_detailDetailView.as_view(),
        name='school_school_contact_detail_detail'
    ),
    url(
        regex=r'^school_contact_detail/$',
        view=School_contact_detailListView.as_view(),
        name='school_school_contact_detail_list'
    ),
    url(
        regex=r'^school_contact_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_contact_detailMonthArchiveView.as_view(),
        name='school_school_contact_detail_month_archive'
    ),
    url(
        regex=r'^school_contact_detail/today/$',
        view=School_contact_detailTodayArchiveView.as_view(),
        name='school_school_contact_detail_today_archive'
    ),
    url(
        regex=r'^school_contact_detail/(?P<pk>\d+?)/update/$',
        view=School_contact_detailUpdateView.as_view(),
        name='school_school_contact_detail_update'
    ),
    url(
        regex=r'^school_contact_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_contact_detailWeekArchiveView.as_view(),
        name='school_school_contact_detail_week_archive'
    ),
    url(
        regex=r'^school_contact_detail/archive/(?P<year>\d{4})/$',
        view=School_contact_detailYearArchiveView.as_view(),
        name='school_school_contact_detail_year_archive'
    ),
)


from school.views.school_recognition_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_recognition/archive/$',
        view=School_recognitionArchiveIndexView.as_view(),
        name='school_school_recognition_archive_index'
    ),
    url(
        regex=r'^school_recognition/create/$',
        view=School_recognitionCreateView.as_view(),
        name='school_school_recognition_create'
    ),
    url(
        regex=r'^school_recognition/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_recognitionDateDetailView.as_view(),
        name='school_school_recognition_date_detail'
    ),
    url(
        regex=r'^school_recognition/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_recognitionDayArchiveView.as_view(),
        name='school_school_recognition_day_archive'
    ),
    url(
        regex=r'^school_recognition/(?P<pk>\d+?)/delete/$',
        view=School_recognitionDeleteView.as_view(),
        name='school_school_recognition_delete'
    ),
    url(
        regex=r'^school_recognition/(?P<pk>\d+?)/$',
        view=School_recognitionDetailView.as_view(),
        name='school_school_recognition_detail'
    ),
    url(
        regex=r'^school_recognition/$',
        view=School_recognitionListView.as_view(),
        name='school_school_recognition_list'
    ),
    url(
        regex=r'^school_recognition/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_recognitionMonthArchiveView.as_view(),
        name='school_school_recognition_month_archive'
    ),
    url(
        regex=r'^school_recognition/today/$',
        view=School_recognitionTodayArchiveView.as_view(),
        name='school_school_recognition_today_archive'
    ),
    url(
        regex=r'^school_recognition/(?P<pk>\d+?)/update/$',
        view=School_recognitionUpdateView.as_view(),
        name='school_school_recognition_update'
    ),
    url(
        regex=r'^school_recognition/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_recognitionWeekArchiveView.as_view(),
        name='school_school_recognition_week_archive'
    ),
    url(
        regex=r'^school_recognition/archive/(?P<year>\d{4})/$',
        view=School_recognitionYearArchiveView.as_view(),
        name='school_school_recognition_year_archive'
    ),
)


from school.views.school_upgradation_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_upgradation/archive/$',
        view=School_upgradationArchiveIndexView.as_view(),
        name='school_school_upgradation_archive_index'
    ),
    url(
        regex=r'^school_upgradation/create/$',
        view=School_upgradationCreateView.as_view(),
        name='school_school_upgradation_create'
    ),
    url(
        regex=r'^school_upgradation/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_upgradationDateDetailView.as_view(),
        name='school_school_upgradation_date_detail'
    ),
    url(
        regex=r'^school_upgradation/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_upgradationDayArchiveView.as_view(),
        name='school_school_upgradation_day_archive'
    ),
    url(
        regex=r'^school_upgradation/(?P<pk>\d+?)/delete/$',
        view=School_upgradationDeleteView.as_view(),
        name='school_school_upgradation_delete'
    ),
    url(
        regex=r'^school_upgradation/(?P<pk>\d+?)/$',
        view=School_upgradationDetailView.as_view(),
        name='school_school_upgradation_detail'
    ),
    url(
        regex=r'^school_upgradation/$',
        view=School_upgradationListView.as_view(),
        name='school_school_upgradation_list'
    ),
    url(
        regex=r'^school_upgradation/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_upgradationMonthArchiveView.as_view(),
        name='school_school_upgradation_month_archive'
    ),
    url(
        regex=r'^school_upgradation/today/$',
        view=School_upgradationTodayArchiveView.as_view(),
        name='school_school_upgradation_today_archive'
    ),
    url(
        regex=r'^school_upgradation/(?P<pk>\d+?)/update/$',
        view=School_upgradationUpdateView.as_view(),
        name='school_school_upgradation_update'
    ),
    url(
        regex=r'^school_upgradation/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_upgradationWeekArchiveView.as_view(),
        name='school_school_upgradation_week_archive'
    ),
    url(
        regex=r'^school_upgradation/archive/(?P<year>\d{4})/$',
        view=School_upgradationYearArchiveView.as_view(),
        name='school_school_upgradation_year_archive'
    ),
)


from school.views.school_residence_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_residence/archive/$',
        view=School_residenceArchiveIndexView.as_view(),
        name='school_school_residence_archive_index'
    ),
    url(
        regex=r'^school_residence/create/$',
        view=School_residenceCreateView.as_view(),
        name='school_school_residence_create'
    ),
    url(
        regex=r'^school_residence/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_residenceDateDetailView.as_view(),
        name='school_school_residence_date_detail'
    ),
    url(
        regex=r'^school_residence/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_residenceDayArchiveView.as_view(),
        name='school_school_residence_day_archive'
    ),
    url(
        regex=r'^school_residence/(?P<pk>\d+?)/delete/$',
        view=School_residenceDeleteView.as_view(),
        name='school_school_residence_delete'
    ),
    url(
        regex=r'^school_residence/(?P<pk>\d+?)/$',
        view=School_residenceDetailView.as_view(),
        name='school_school_residence_detail'
    ),
    url(
        regex=r'^school_residence/$',
        view=School_residenceListView.as_view(),
        name='school_school_residence_list'
    ),
    url(
        regex=r'^school_residence/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_residenceMonthArchiveView.as_view(),
        name='school_school_residence_month_archive'
    ),
    url(
        regex=r'^school_residence/today/$',
        view=School_residenceTodayArchiveView.as_view(),
        name='school_school_residence_today_archive'
    ),
    url(
        regex=r'^school_residence/(?P<pk>\d+?)/update/$',
        view=School_residenceUpdateView.as_view(),
        name='school_school_residence_update'
    ),
    url(
        regex=r'^school_residence/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_residenceWeekArchiveView.as_view(),
        name='school_school_residence_week_archive'
    ),
    url(
        regex=r'^school_residence/archive/(?P<year>\d{4})/$',
        view=School_residenceYearArchiveView.as_view(),
        name='school_school_residence_year_archive'
    ),
)


from school.views.school_anganwadi_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_anganwadi/archive/$',
        view=School_anganwadiArchiveIndexView.as_view(),
        name='school_school_anganwadi_archive_index'
    ),
    url(
        regex=r'^school_anganwadi/create/$',
        view=School_anganwadiCreateView.as_view(),
        name='school_school_anganwadi_create'
    ),
    url(
        regex=r'^school_anganwadi/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_anganwadiDateDetailView.as_view(),
        name='school_school_anganwadi_date_detail'
    ),
    url(
        regex=r'^school_anganwadi/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_anganwadiDayArchiveView.as_view(),
        name='school_school_anganwadi_day_archive'
    ),
    url(
        regex=r'^school_anganwadi/(?P<pk>\d+?)/delete/$',
        view=School_anganwadiDeleteView.as_view(),
        name='school_school_anganwadi_delete'
    ),
    url(
        regex=r'^school_anganwadi/(?P<pk>\d+?)/$',
        view=School_anganwadiDetailView.as_view(),
        name='school_school_anganwadi_detail'
    ),
    url(
        regex=r'^school_anganwadi/$',
        view=School_anganwadiListView.as_view(),
        name='school_school_anganwadi_list'
    ),
    url(
        regex=r'^school_anganwadi/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_anganwadiMonthArchiveView.as_view(),
        name='school_school_anganwadi_month_archive'
    ),
    url(
        regex=r'^school_anganwadi/today/$',
        view=School_anganwadiTodayArchiveView.as_view(),
        name='school_school_anganwadi_today_archive'
    ),
    url(
        regex=r'^school_anganwadi/(?P<pk>\d+?)/update/$',
        view=School_anganwadiUpdateView.as_view(),
        name='school_school_anganwadi_update'
    ),
    url(
        regex=r'^school_anganwadi/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_anganwadiWeekArchiveView.as_view(),
        name='school_school_anganwadi_week_archive'
    ),
    url(
        regex=r'^school_anganwadi/archive/(?P<year>\d{4})/$',
        view=School_anganwadiYearArchiveView.as_view(),
        name='school_school_anganwadi_year_archive'
    ),
)


from school.views.school_crc_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_crc/archive/$',
        view=School_crcArchiveIndexView.as_view(),
        name='school_school_crc_archive_index'
    ),
    url(
        regex=r'^school_crc/create/$',
        view=School_crcCreateView.as_view(),
        name='school_school_crc_create'
    ),
    url(
        regex=r'^school_crc/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_crcDateDetailView.as_view(),
        name='school_school_crc_date_detail'
    ),
    url(
        regex=r'^school_crc/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_crcDayArchiveView.as_view(),
        name='school_school_crc_day_archive'
    ),
    url(
        regex=r'^school_crc/(?P<pk>\d+?)/delete/$',
        view=School_crcDeleteView.as_view(),
        name='school_school_crc_delete'
    ),
    url(
        regex=r'^school_crc/(?P<pk>\d+?)/$',
        view=School_crcDetailView.as_view(),
        name='school_school_crc_detail'
    ),
    url(
        regex=r'^school_crc/$',
        view=School_crcListView.as_view(),
        name='school_school_crc_list'
    ),
    url(
        regex=r'^school_crc/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_crcMonthArchiveView.as_view(),
        name='school_school_crc_month_archive'
    ),
    url(
        regex=r'^school_crc/today/$',
        view=School_crcTodayArchiveView.as_view(),
        name='school_school_crc_today_archive'
    ),
    url(
        regex=r'^school_crc/(?P<pk>\d+?)/update/$',
        view=School_crcUpdateView.as_view(),
        name='school_school_crc_update'
    ),
    url(
        regex=r'^school_crc/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_crcWeekArchiveView.as_view(),
        name='school_school_crc_week_archive'
    ),
    url(
        regex=r'^school_crc/archive/(?P<year>\d{4})/$',
        view=School_crcYearArchiveView.as_view(),
        name='school_school_crc_year_archive'
    ),
)


from school.views.school_brc_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_brc/archive/$',
        view=School_brcArchiveIndexView.as_view(),
        name='school_school_brc_archive_index'
    ),
    url(
        regex=r'^school_brc/create/$',
        view=School_brcCreateView.as_view(),
        name='school_school_brc_create'
    ),
    url(
        regex=r'^school_brc/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_brcDateDetailView.as_view(),
        name='school_school_brc_date_detail'
    ),
    url(
        regex=r'^school_brc/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_brcDayArchiveView.as_view(),
        name='school_school_brc_day_archive'
    ),
    url(
        regex=r'^school_brc/(?P<pk>\d+?)/delete/$',
        view=School_brcDeleteView.as_view(),
        name='school_school_brc_delete'
    ),
    url(
        regex=r'^school_brc/(?P<pk>\d+?)/$',
        view=School_brcDetailView.as_view(),
        name='school_school_brc_detail'
    ),
    url(
        regex=r'^school_brc/$',
        view=School_brcListView.as_view(),
        name='school_school_brc_list'
    ),
    url(
        regex=r'^school_brc/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_brcMonthArchiveView.as_view(),
        name='school_school_brc_month_archive'
    ),
    url(
        regex=r'^school_brc/today/$',
        view=School_brcTodayArchiveView.as_view(),
        name='school_school_brc_today_archive'
    ),
    url(
        regex=r'^school_brc/(?P<pk>\d+?)/update/$',
        view=School_brcUpdateView.as_view(),
        name='school_school_brc_update'
    ),
    url(
        regex=r'^school_brc/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_brcWeekArchiveView.as_view(),
        name='school_school_brc_week_archive'
    ),
    url(
        regex=r'^school_brc/archive/(?P<year>\d{4})/$',
        view=School_brcYearArchiveView.as_view(),
        name='school_school_brc_year_archive'
    ),
)


from school.views.school_detail_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_detail/archive/$',
        view=School_detailArchiveIndexView.as_view(),
        name='school_school_detail_archive_index'
    ),
    url(
        regex=r'^school_detail/create/$',
        view=School_detailCreateView.as_view(),
        name='school_school_detail_create'
    ),
    url(
        regex=r'^school_detail/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_detailDateDetailView.as_view(),
        name='school_school_detail_date_detail'
    ),
    url(
        regex=r'^school_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_detailDayArchiveView.as_view(),
        name='school_school_detail_day_archive'
    ),
    url(
        regex=r'^school_detail/(?P<pk>\d+?)/delete/$',
        view=School_detailDeleteView.as_view(),
        name='school_school_detail_delete'
    ),
    url(
        regex=r'^school_detail/(?P<pk>\d+?)/$',
        view=School_detailDetailView.as_view(),
        name='school_school_detail_detail'
    ),
    url(
        regex=r'^school_detail/$',
        view=School_detailListView.as_view(),
        name='school_school_detail_list'
    ),
    url(
        regex=r'^school_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_detailMonthArchiveView.as_view(),
        name='school_school_detail_month_archive'
    ),
    url(
        regex=r'^school_detail/today/$',
        view=School_detailTodayArchiveView.as_view(),
        name='school_school_detail_today_archive'
    ),
    url(
        regex=r'^school_detail/(?P<pk>\d+?)/update/$',
        view=School_detailUpdateView.as_view(),
        name='school_school_detail_update'
    ),
    url(
        regex=r'^school_detail/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_detailWeekArchiveView.as_view(),
        name='school_school_detail_week_archive'
    ),
    url(
        regex=r'^school_detail/archive/(?P<year>\d{4})/$',
        view=School_detailYearArchiveView.as_view(),
        name='school_school_detail_year_archive'
    ),
)


from school.views.school_flag_views import *
urlpatterns += patterns('',
    url(
        regex=r'^school_flag/archive/$',
        view=School_flagArchiveIndexView.as_view(),
        name='school_school_flag_archive_index'
    ),
    url(
        regex=r'^school_flag/create/$',
        view=School_flagCreateView.as_view(),
        name='school_school_flag_create'
    ),
    url(
        regex=r'^school_flag/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/'
               '(?P<pk>\d+?)/$',
        view=School_flagDateDetailView.as_view(),
        name='school_school_flag_date_detail'
    ),
    url(
        regex=r'^school_flag/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               '(?P<day>\d{1,2})/$',
        view=School_flagDayArchiveView.as_view(),
        name='school_school_flag_day_archive'
    ),
    url(
        regex=r'^school_flag/(?P<pk>\d+?)/delete/$',
        view=School_flagDeleteView.as_view(),
        name='school_school_flag_delete'
    ),
    url(
        regex=r'^school_flag/(?P<pk>\d+?)/$',
        view=School_flagDetailView.as_view(),
        name='school_school_flag_detail'
    ),
    url(
        regex=r'^school_flag/$',
        view=School_flagListView.as_view(),
        name='school_school_flag_list'
    ),
    url(
        regex=r'^school_flag/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/$',
        view=School_flagMonthArchiveView.as_view(),
        name='school_school_flag_month_archive'
    ),
    url(
        regex=r'^school_flag/today/$',
        view=School_flagTodayArchiveView.as_view(),
        name='school_school_flag_today_archive'
    ),
    url(
        regex=r'^school_flag/(?P<pk>\d+?)/update/$',
        view=School_flagUpdateView.as_view(),
        name='school_school_flag_update'
    ),
    url(
        regex=r'^school_flag/archive/(?P<year>\d{4})/'
               '(?P<month>\d{1,2})/'
               'week/(?P<week>\d{1,2})/$',
        view=School_flagWeekArchiveView.as_view(),
        name='school_school_flag_week_archive'
    ),
    url(
        regex=r'^school_flag/archive/(?P<year>\d{4})/$',
        view=School_flagYearArchiveView.as_view(),
        name='school_school_flag_year_archive'
    ),
)
