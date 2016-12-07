from django.conf.urls import patterns, url



from baseapp.views.district_views import *
urlpatterns = patterns('',

    url(
        regex=r'^district/create/$',
        view=DistrictCreateView.as_view(),
        name='baseapp_district_create'
    ),


    url(
        regex=r'^district/(?P<pk>\d+?)/delete/$',
        view=DistrictDeleteView.as_view(),
        name='baseapp_district_delete'
    ),
    url(
        regex=r'^district/(?P<pk>\d+?)/$',
        view=DistrictDetailView.as_view(),
        name='baseapp_district_detail'
    ),
    url(
        regex=r'^district/$',
        view=DistrictListView.as_view(),
        name='baseapp_district_list'
    ),


    url(
        regex=r'^district/(?P<pk>\d+?)/update/$',
        view=DistrictUpdateView.as_view(),
        name='baseapp_district_update'
    ),


)


from baseapp.views.block_views import *
urlpatterns += patterns('',

    url(
        regex=r'^block/create/$',
        view=BlockCreateView.as_view(),
        name='baseapp_block_create'
    ),


    url(
        regex=r'^block/(?P<pk>\d+?)/delete/$',
        view=BlockDeleteView.as_view(),
        name='baseapp_block_delete'
    ),
    url(
        regex=r'^block/(?P<pk>\d+?)/$',
        view=BlockDetailView.as_view(),
        name='baseapp_block_detail'
    ),
    url(
        regex=r'^block/$',
        view=BlockListView.as_view(),
        name='baseapp_block_list'
    ),


    url(
        regex=r'^block/(?P<pk>\d+?)/update/$',
        view=BlockUpdateView.as_view(),
        name='baseapp_block_update'
    ),


)


from baseapp.views.assembly_views import *
urlpatterns += patterns('',

    url(
        regex=r'^assembly/create/$',
        view=AssemblyCreateView.as_view(),
        name='baseapp_assembly_create'
    ),


    url(
        regex=r'^assembly/(?P<pk>\d+?)/delete/$',
        view=AssemblyDeleteView.as_view(),
        name='baseapp_assembly_delete'
    ),
    url(
        regex=r'^assembly/(?P<pk>\d+?)/$',
        view=AssemblyDetailView.as_view(),
        name='baseapp_assembly_detail'
    ),
    url(
        regex=r'^assembly/$',
        view=AssemblyListView.as_view(),
        name='baseapp_assembly_list'
    ),


    url(
        regex=r'^assembly/(?P<pk>\d+?)/update/$',
        view=AssemblyUpdateView.as_view(),
        name='baseapp_assembly_update'
    ),


)


from baseapp.views.parliamentary_views import *
urlpatterns += patterns('',

    url(
        regex=r'^parliamentary/create/$',
        view=ParliamentaryCreateView.as_view(),
        name='baseapp_parliamentary_create'
    ),


    url(
        regex=r'^parliamentary/(?P<pk>\d+?)/delete/$',
        view=ParliamentaryDeleteView.as_view(),
        name='baseapp_parliamentary_delete'
    ),
    url(
        regex=r'^parliamentary/(?P<pk>\d+?)/$',
        view=ParliamentaryDetailView.as_view(),
        name='baseapp_parliamentary_detail'
    ),
    url(
        regex=r'^parliamentary/$',
        view=ParliamentaryListView.as_view(),
        name='baseapp_parliamentary_list'
    ),


    url(
        regex=r'^parliamentary/(?P<pk>\d+?)/update/$',
        view=ParliamentaryUpdateView.as_view(),
        name='baseapp_parliamentary_update'
    ),


)



from baseapp.views.habitation_views import *
urlpatterns += patterns('',

    url(
        regex=r'^habitation/create/$',
        view=HabitationCreateView.as_view(),
        name='baseapp_habitation_create'
    ),


    url(
        regex=r'^habitation/(?P<pk>\d+?)/delete/$',
        view=HabitationDeleteView.as_view(),
        name='baseapp_habitation_delete'
    ),
    url(
        regex=r'^habitation/(?P<pk>\d+?)/$',
        view=HabitationDetailView.as_view(),
        name='baseapp_habitation_detail'
    ),
    url(
        regex=r'^habitation/$',
        view=HabitationListView.as_view(),
        name='baseapp_habitation_list'
    ),


    url(
        regex=r'^habitation/(?P<pk>\d+?)/update/$',
        view=HabitationUpdateView.as_view(),
        name='baseapp_habitation_update'
    ),


)


from baseapp.views.management_views import *
urlpatterns += patterns('',

    url(
        regex=r'^management/create/$',
        view=ManagementCreateView.as_view(),
        name='baseapp_management_create'
    ),


    url(
        regex=r'^management/(?P<pk>\d+?)/delete/$',
        view=ManagementDeleteView.as_view(),
        name='baseapp_management_delete'
    ),
    url(
        regex=r'^management/(?P<pk>\d+?)/$',
        view=ManagementDetailView.as_view(),
        name='baseapp_management_detail'
    ),
    url(
        regex=r'^management/$',
        view=ManagementListView.as_view(),
        name='baseapp_management_list'
    ),


    url(
        regex=r'^management/(?P<pk>\d+?)/update/$',
        view=ManagementUpdateView.as_view(),
        name='baseapp_management_update'
    ),


)

from baseapp.views.category_views import *
urlpatterns += patterns('',

    url(
        regex=r'^category/create/$',
        view=CategoryCreateView.as_view(),
        name='baseapp_category_create'
    ),


    url(
        regex=r'^category/(?P<pk>\d+?)/delete/$',
        view=CategoryDeleteView.as_view(),
        name='baseapp_category_delete'
    ),
    url(
        regex=r'^category/(?P<pk>\d+?)/$',
        view=CategoryDetailView.as_view(),
        name='baseapp_category_detail'
    ),
    url(
        regex=r'^category/$',
        view=CategoryListView.as_view(),
        name='baseapp_category_list'
    ),


    url(
        regex=r'^category/(?P<pk>\d+?)/update/$',
        view=CategoryUpdateView.as_view(),
        name='baseapp_category_update'
    ),


)
from baseapp.views.school_views import *
urlpatterns += patterns('',

    url(
        regex=r'^school/create/$',
        view=SchoolCreateView.as_view(),
        name='baseapp_school_create'
    ),


    url(
        regex=r'^school/(?P<pk>\d+?)/delete/$',
        view=SchoolDeleteView.as_view(),
        name='baseapp_school_delete'
    ),
    url(
        regex=r'^school/(?P<pk>\d+?)/$',
        view=SchoolDetailView.as_view(),
        name='baseapp_school_detail'
    ),
    url(
        regex=r'^school/$',
        view=SchoolListView.as_view(),
        name='baseapp_school_list'
    ),


    url(
        regex=r'^school/(?P<pk>\d+?)/update/$',
        view=SchoolUpdateView.as_view(),
        name='baseapp_school_update'
    ),


)


from baseapp.views.taluk_views import *
urlpatterns += patterns('',

    url(
        regex=r'^taluk/create/$',
        view=TalukCreateView.as_view(),
        name='baseapp_taluk_create'
    ),


    url(
        regex=r'^taluk/(?P<pk>\d+?)/delete/$',
        view=TalukDeleteView.as_view(),
        name='baseapp_taluk_delete'
    ),
    url(
        regex=r'^taluk/(?P<pk>\d+?)/$',
        view=TalukDetailView.as_view(),
        name='baseapp_taluk_detail'
    ),
    url(
        regex=r'^taluk/$',
        view=TalukListView.as_view(),
        name='baseapp_taluk_list'
    ),


    url(
        regex=r'^taluk/(?P<pk>\d+?)/update/$',
        view=TalukUpdateView.as_view(),
        name='baseapp_taluk_update'
    ),


)


from baseapp.views.educational_district_views import *
urlpatterns += patterns('',

    url(
        regex=r'^educational_district/create/$',
        view=Educational_districtCreateView.as_view(),
        name='baseapp_educational_district_create'
    ),


    url(
        regex=r'^educational_district/(?P<pk>\d+?)/delete/$',
        view=Educational_districtDeleteView.as_view(),
        name='baseapp_educational_district_delete'
    ),
    url(
        regex=r'^educational_district/(?P<pk>\d+?)/$',
        view=Educational_districtDetailView.as_view(),
        name='baseapp_educational_district_detail'
    ),
    url(
        regex=r'^educational_district/$',
        view=Educational_districtListView.as_view(),
        name='baseapp_educational_district_list'
    ),


    url(
        regex=r'^educational_district/(?P<pk>\d+?)/update/$',
        view=Educational_districtUpdateView.as_view(),
        name='baseapp_educational_district_update'
    ),


)


from baseapp.views.educational_block_views import *
urlpatterns += patterns('',

    url(
        regex=r'^educational_block/create/$',
        view=Educational_blockCreateView.as_view(),
        name='baseapp_educational_block_create'
    ),


    url(
        regex=r'^educational_block/(?P<pk>\d+?)/delete/$',
        view=Educational_blockDeleteView.as_view(),
        name='baseapp_educational_block_delete'
    ),
    url(
        regex=r'^educational_block/(?P<pk>\d+?)/$',
        view=Educational_blockDetailView.as_view(),
        name='baseapp_educational_block_detail'
    ),
    url(
        regex=r'^educational_block/$',
        view=Educational_blockListView.as_view(),
        name='baseapp_educational_block_list'
    ),


    url(
        regex=r'^educational_block/(?P<pk>\d+?)/update/$',
        view=Educational_blockUpdateView.as_view(),
        name='baseapp_educational_block_update'
    ),


)


from baseapp.views.revenue_block_views import *
urlpatterns += patterns('',

    url(
        regex=r'^revenue_block/create/$',
        view=Revenue_blockCreateView.as_view(),
        name='baseapp_revenue_block_create'
    ),


    url(
        regex=r'^revenue_block/(?P<pk>\d+?)/delete/$',
        view=Revenue_blockDeleteView.as_view(),
        name='baseapp_revenue_block_delete'
    ),
    url(
        regex=r'^revenue_block/(?P<pk>\d+?)/$',
        view=Revenue_blockDetailView.as_view(),
        name='baseapp_revenue_block_detail'
    ),
    url(
        regex=r'^revenue_block/$',
        view=Revenue_blockListView.as_view(),
        name='baseapp_revenue_block_list'
    ),


    url(
        regex=r'^revenue_block/(?P<pk>\d+?)/update/$',
        view=Revenue_blockUpdateView.as_view(),
        name='baseapp_revenue_block_update'
    ),


)


from baseapp.views.community_views import *
urlpatterns += patterns('',

    url(
        regex=r'^community/create/$',
        view=CommunityCreateView.as_view(),
        name='baseapp_community_create'
    ),


    url(
        regex=r'^community/(?P<pk>\d+?)/delete/$',
        view=CommunityDeleteView.as_view(),
        name='baseapp_community_delete'
    ),
    url(
        regex=r'^community/(?P<pk>\d+?)/$',
        view=CommunityDetailView.as_view(),
        name='baseapp_community_detail'
    ),
    url(
        regex=r'^community/$',
        view=CommunityListView.as_view(),
        name='baseapp_community_list'
    ),


    url(
        regex=r'^community/(?P<pk>\d+?)/update/$',
        view=CommunityUpdateView.as_view(),
        name='baseapp_community_update'
    ),


)


from baseapp.views.religion_views import *
urlpatterns += patterns('',

    url(
        regex=r'^religion/create/$',
        view=ReligionCreateView.as_view(),
        name='baseapp_religion_create'
    ),


    url(
        regex=r'^religion/(?P<pk>\d+?)/delete/$',
        view=ReligionDeleteView.as_view(),
        name='baseapp_religion_delete'
    ),
    url(
        regex=r'^religion/(?P<pk>\d+?)/$',
        view=ReligionDetailView.as_view(),
        name='baseapp_religion_detail'
    ),
    url(
        regex=r'^religion/$',
        view=ReligionListView.as_view(),
        name='baseapp_religion_list'
    ),


    url(
        regex=r'^religion/(?P<pk>\d+?)/update/$',
        view=ReligionUpdateView.as_view(),
        name='baseapp_religion_update'
    ),


)


from baseapp.views.language_views import *
urlpatterns += patterns('',

    url(
        regex=r'^language/create/$',
        view=LanguageCreateView.as_view(),
        name='baseapp_language_create'
    ),


    url(
        regex=r'^language/(?P<pk>\d+?)/delete/$',
        view=LanguageDeleteView.as_view(),
        name='baseapp_language_delete'
    ),
    url(
        regex=r'^language/(?P<pk>\d+?)/$',
        view=LanguageDetailView.as_view(),
        name='baseapp_language_detail'
    ),
    url(
        regex=r'^language/$',
        view=LanguageListView.as_view(),
        name='baseapp_language_list'
    ),


    url(
        regex=r'^language/(?P<pk>\d+?)/update/$',
        view=LanguageUpdateView.as_view(),
        name='baseapp_language_update'
    ),


)


from baseapp.views.differently_abled_views import *
urlpatterns += patterns('',

    url(
        regex=r'^differently_abled/create/$',
        view=Differently_abledCreateView.as_view(),
        name='baseapp_differently_abled_create'
    ),


    url(
        regex=r'^differently_abled/(?P<pk>\d+?)/delete/$',
        view=Differently_abledDeleteView.as_view(),
        name='baseapp_differently_abled_delete'
    ),
    url(
        regex=r'^differently_abled/(?P<pk>\d+?)/$',
        view=Differently_abledDetailView.as_view(),
        name='baseapp_differently_abled_detail'
    ),
    url(
        regex=r'^differently_abled/$',
        view=Differently_abledListView.as_view(),
        name='baseapp_differently_abled_list'
    ),


    url(
        regex=r'^differently_abled/(?P<pk>\d+?)/update/$',
        view=Differently_abledUpdateView.as_view(),
        name='baseapp_differently_abled_update'
    ),


)


from baseapp.views.disadvantaged_group_views import *
urlpatterns += patterns('',

    url(
        regex=r'^disadvantaged_group/create/$',
        view=Disadvantaged_groupCreateView.as_view(),
        name='baseapp_disadvantaged_group_create'
    ),


    url(
        regex=r'^disadvantaged_group/(?P<pk>\d+?)/delete/$',
        view=Disadvantaged_groupDeleteView.as_view(),
        name='baseapp_disadvantaged_group_delete'
    ),
    url(
        regex=r'^disadvantaged_group/(?P<pk>\d+?)/$',
        view=Disadvantaged_groupDetailView.as_view(),
        name='baseapp_disadvantaged_group_detail'
    ),
    url(
        regex=r'^disadvantaged_group/$',
        view=Disadvantaged_groupListView.as_view(),
        name='baseapp_disadvantaged_group_list'
    ),


    url(
        regex=r'^disadvantaged_group/(?P<pk>\d+?)/update/$',
        view=Disadvantaged_groupUpdateView.as_view(),
        name='baseapp_disadvantaged_group_update'
    ),


)


from baseapp.views.schemes_views import *
urlpatterns += patterns('',

    url(
        regex=r'^schemes/create/$',
        view=SchemesCreateView.as_view(),
        name='baseapp_schemes_create'
    ),


    url(
        regex=r'^schemes/(?P<pk>\d+?)/delete/$',
        view=SchemesDeleteView.as_view(),
        name='baseapp_schemes_delete'
    ),
    url(
        regex=r'^schemes/(?P<pk>\d+?)/$',
        view=SchemesDetailView.as_view(),
        name='baseapp_schemes_detail'
    ),
    url(
        regex=r'^schemes/$',
        view=SchemesListView.as_view(),
        name='baseapp_schemes_list'
    ),


    url(
        regex=r'^schemes/(?P<pk>\d+?)/update/$',
        view=SchemesUpdateView.as_view(),
        name='baseapp_schemes_update'
    ),


)

from baseapp.views.academic_year_views import *
urlpatterns += patterns('',

    url(
        regex=r'^academic_year/create/$',
        view=Academic_YearCreateView.as_view(),
        name='baseapp_academic_year_create'
    ),

    url(
        regex=r'^academic_year/(?P<pk>\d+?)/delete/$',
        view=Academic_YearDeleteView.as_view(),
        name='baseapp_academic_year_delete'
    ),
    url(
        regex=r'^academic_year/(?P<pk>\d+?)/$',
        view=Academic_YearDetailView.as_view(),
        name='baseapp_academic_year_detail'
    ),
    url(
        regex=r'^academic_year/$',
        view=Academic_YearListView.as_view(),
        name='baseapp_academic_year_list'
    ),


    url(
        regex=r'^academic_year/(?P<pk>\d+?)/update/$',
        view=Academic_YearUpdateView.as_view(),
        name='baseapp_academic_year_update'
    ),

)

from baseapp.views.bank_views import *
urlpatterns += patterns('',

    url(
        regex=r'^bank/create/$',
        view=BankCreateView.as_view(),
        name='baseapp_bank_create'
    ),


    url(
        regex=r'^bank/(?P<pk>\d+?)/delete/$',
        view=BankDeleteView.as_view(),
        name='baseapp_bank_delete'
    ),
    url(
        regex=r'^bank/(?P<pk>\d+?)/$',
        view=BankDetailView.as_view(),
        name='baseapp_bank_detail'
    ),
    url(
        regex=r'^bank/$',
        view=BankListView.as_view(),
        name='baseapp_bank_list'
    ),


    url(
        regex=r'^bank/(?P<pk>\d+?)/update/$',
        view=BankUpdateView.as_view(),
        name='baseapp_bank_update'
    ),

)

from baseapp.views.education_medium_views import *
urlpatterns += patterns('',

    url(
        regex=r'^education_medium/create/$',
        view=Education_mediumCreateView.as_view(),
        name='baseapp_education_medium_create'
    ),


    url(
        regex=r'^education_medium/(?P<pk>\d+?)/delete/$',
        view=Education_mediumDeleteView.as_view(),
        name='baseapp_education_medium_delete'
    ),
    url(
        regex=r'^education_medium/(?P<pk>\d+?)/$',
        view=Education_mediumDetailView.as_view(),
        name='baseapp_education_medium_detail'
    ),
    url(
        regex=r'^education_medium/$',
        view=Education_mediumListView.as_view(),
        name='baseapp_education_medium_list'
    ),

    url(
        regex=r'^education_medium/(?P<pk>\d+?)/update/$',
        view=Education_mediumUpdateView.as_view(),
        name='baseapp_education_medium_update'
    ),

)


from baseapp.views.zone_views import *
urlpatterns += patterns('',

    url(
        regex=r'^zone/create/$',
        view=ZoneCreateView.as_view(),
        name='baseapp_zone_create'
    ),

    url(
        regex=r'^zone/(?P<pk>\d+?)/delete/$',
        view=ZoneDeleteView.as_view(),
        name='baseapp_zone_delete'
    ),
    url(
        regex=r'^zone/(?P<pk>\d+?)/$',
        view=ZoneDetailView.as_view(),
        name='baseapp_zone_detail'
    ),
    url(
        regex=r'^zone/$',
        view=ZoneListView.as_view(),
        name='baseapp_zone_list'
    ),

    url(
        regex=r'^zone/(?P<pk>\d+?)/update/$',
        view=ZoneUpdateView.as_view(),
        name='baseapp_zone_update'
    ),

)

from baseapp.views.sub_castes_views import *
urlpatterns += patterns('',

    url(
        regex=r'^sub_castes/create/$',
        view=Sub_CastesCreateView.as_view(),
        name='baseapp_sub_castes_create'
    ),

    url(
        regex=r'^sub_castes/(?P<pk>\d+?)/delete/$',
        view=Sub_CastesDeleteView.as_view(),
        name='baseapp_sub_castes_delete'
    ),
    url(
        regex=r'^sub_castes/(?P<pk>\d+?)/$',
        view=Sub_CastesDetailView.as_view(),
        name='baseapp_sub_castes_detail'
    ),
    url(
        regex=r'^sub_castes/$',
        view=Sub_CastesListView.as_view(),
        name='baseapp_sub_castes_list'
    ),

    url(
        regex=r'^sub_castes/(?P<pk>\d+?)/update/$',
        view=Sub_CastesUpdateView.as_view(),
        name='baseapp_sub_castes_update'
    ),

)

from baseapp.views.nationality_views import *
urlpatterns += patterns('',

    url(
        regex=r'^nationality/create/$',
        view=NationalityCreateView.as_view(),
        name='baseapp_nationality_create'
    ),

    url(
        regex=r'^nationality/(?P<pk>\d+?)/delete/$',
        view=NationalityDeleteView.as_view(),
        name='baseapp_nationality_delete'
    ),
    url(
        regex=r'^nationality/(?P<pk>\d+?)/$',
        view=NationalityDetailView.as_view(),
        name='baseapp_nationality_detail'
    ),
    url(
        regex=r'^nationality/$',
        view=NationalityListView.as_view(),
        name='baseapp_nationality_list'
    ),

    url(
        regex=r'^nationality/(?P<pk>\d+?)/update/$',
        view=NationalityUpdateView.as_view(),
        name='baseapp_nationality_update'
    ),

)

from baseapp.views.class_studying_views import *
urlpatterns += patterns('',

    url(
        regex=r'^class_studying/create/$',
        view=Class_StudyingCreateView.as_view(),
        name='baseapp_class_studying_create'
    ),

    url(
        regex=r'^class_studying/(?P<pk>\d+?)/delete/$',
        view=Class_StudyingDeleteView.as_view(),
        name='baseapp_class_studying_delete'
    ),
    url(
        regex=r'^class_studying/(?P<pk>\d+?)/$',
        view=Class_StudyingDetailView.as_view(),
        name='baseapp_class_studying_detail'
    ),
    url(
        regex=r'^class_studying/$',
        view=Class_StudyingListView.as_view(),
        name='baseapp_class_studying_list'
    ),

    url(
        regex=r'^class_studying/(?P<pk>\d+?)/update/$',
        view=Class_StudyingUpdateView.as_view(),
        name='baseapp_class_studying_update'
    ),

)

from baseapp.views.group_code_views import *
urlpatterns += patterns('',

    url(
        regex=r'^group_code/create/$',
        view=Group_codeCreateView.as_view(),
        name='baseapp_group_code_create'
    ),

    url(
        regex=r'^group_code/(?P<pk>\d+?)/delete/$',
        view=Group_codeDeleteView.as_view(),
        name='baseapp_group_code_delete'
    ),
    url(
        regex=r'^group_code/(?P<pk>\d+?)/$',
        view=Group_codeDetailView.as_view(),
        name='baseapp_group_code_detail'
    ),
    url(
        regex=r'^group_code/$',
        view=Group_codeListView.as_view(),
        name='baseapp_group_code_list'
    ),

    url(
        regex=r'^group_code/(?P<pk>\d+?)/update/$',
        view=Group_codeUpdateView.as_view(),
        name='baseapp_group_code_update'
    ),

)
