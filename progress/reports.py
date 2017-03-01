from django.views.generic import View,ListView, DetailView, CreateView, \
    DeleteView, UpdateView, \
    ArchiveIndexView, DateDetailView, \
    DayArchiveView, MonthArchiveView, \
    TodayArchiveView, WeekArchiveView, \
    YearArchiveView
from django.shortcuts import *
from students.models import *
from django.db.models import *
from baseapp.models import *
from progress.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger
from django import template
from django.contrib import messages
from excel_response import ExcelResponse
from django.utils import simplejson
import os
from django.conf import settings
from django.core.files.base import ContentFile







class School_level_progress_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        school_id=School.objects.get(id=school)
        emis_students=School_child_count.objects.get(school_id=school_id)
        emis_count_one=emis_students.one
        emis_count_two=emis_students.two
        emis_count_three=emis_students.three
        emis_count_four=emis_students.four
        emis_count_five=emis_students.five
        emis_count_six=emis_students.six
        emis_count_seven=emis_students.seven
        emis_count_eight=emis_students.eight
        emis_count_nine=emis_students.nine
        emis_count_ten=emis_students.ten
        emis_count_eleven=emis_students.eleven
        emis_count_twelve=emis_students.twelve
        emis_count_total_count=emis_students.total_count
        return render(request,'school/school_progress_report.html',locals())
        


class Block_level_progress_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2]
        block=self.kwargs['pk']
        block_name=Block.objects.get(id=block)
        school_list=School.objects.filter(block_id=block).order_by('management_id')
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        block_emis_one=emis_count.aggregate(Sum('one')).values()[0]
        block_emis_two=emis_count.aggregate(Sum('two')).values()[0]
        block_emis_three=emis_count.aggregate(Sum('three')).values()[0]
        block_emis_four=emis_count.aggregate(Sum('four')).values()[0]
        block_emis_five=emis_count.aggregate(Sum('five')).values()[0]
        block_emis_six=emis_count.aggregate(Sum('six')).values()[0]
        block_emis_seven=emis_count.aggregate(Sum('seven')).values()[0]
        block_emis_eight=emis_count.aggregate(Sum('eight')).values()[0]
        block_emis_nine=emis_count.aggregate(Sum('nine')).values()[0]
        block_emis_ten=emis_count.aggregate(Sum('ten')).values()[0]
        block_emis_eleven=emis_count.aggregate(Sum('eleven')).values()[0]
        block_emis_twelve=emis_count.aggregate(Sum('twelve')).values()[0]
        block_emis_total_count=emis_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'block/block_progress_report.html',locals())
   
      
class District_level_progress_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3]
        user=self.kwargs['pk']
        district=District.objects.get(id=user)
        blocks=Block.objects.filter(district_id=user) 
        block_ids=[]
        block_names=[]
        block_emis_one=[]
        block_emis_two=[]
        block_emis_three=[]
        block_emis_four=[]
        block_emis_five=[]
        block_emis_six=[]
        block_emis_seven=[]
        block_emis_eight=[]
        block_emis_nine=[]
        block_emis_ten=[]
        block_emis_eleven=[]
        block_emis_twelve=[]
        block_emis_total_count=[]
        for i in blocks:
            block_ids.append(str(i.id))
            block_names.append(i.block_name)
            school_list=School.objects.filter(block_id=i.id)
            emis_count=School_child_count.objects.filter(school_id__in=school_list)
            block_emis_total_one=emis_count.aggregate(Sum('one'))
            block_emis_total_two=emis_count.aggregate(Sum('two'))
            block_emis_total_three=emis_count.aggregate(Sum('three'))
            block_emis_total_four=emis_count.aggregate(Sum('four'))
            block_emis_total_five=emis_count.aggregate(Sum('five'))
            block_emis_total_six=emis_count.aggregate(Sum('six'))
            block_emis_total_seven=emis_count.aggregate(Sum('seven'))
            block_emis_total_eight=emis_count.aggregate(Sum('eight'))
            block_emis_total_nine=emis_count.aggregate(Sum('nine'))
            block_emis_total_ten=emis_count.aggregate(Sum('ten'))
            block_emis_total_eleven=emis_count.aggregate(Sum('eleven'))
            block_emis_total_twelve=emis_count.aggregate(Sum('twelve'))
            block_emis_total_total_count=emis_count.aggregate(Sum('total_count'))
            block_emis_one+=block_emis_total_one.values()
            block_emis_two+=block_emis_total_two.values()
            block_emis_three+=block_emis_total_three.values()
            block_emis_four+=block_emis_total_four.values()
            block_emis_five+=block_emis_total_five.values()
            block_emis_six+=block_emis_total_six.values()
            block_emis_seven+=block_emis_total_seven.values()
            block_emis_eight+=block_emis_total_eight.values()
            block_emis_nine+=block_emis_total_nine.values()
            block_emis_ten+=block_emis_total_ten.values()
            block_emis_eleven+=block_emis_total_eleven.values()
            block_emis_twelve+=block_emis_total_twelve.values()
            block_emis_total_count+=block_emis_total_total_count.values()
        mylist=zip(block_ids,block_names,block_emis_one,block_emis_two,block_emis_three,block_emis_four,block_emis_five,block_emis_six,block_emis_seven,block_emis_eight,block_emis_nine,block_emis_ten,block_emis_eleven,block_emis_twelve,block_emis_total_count)
        school_list=School.objects.filter(district_id=district)
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        district_emis_one=emis_count.aggregate(Sum('one')).values()[0]
        district_emis_two=emis_count.aggregate(Sum('two')).values()[0]
        district_emis_three=emis_count.aggregate(Sum('three')).values()[0]
        district_emis_four=emis_count.aggregate(Sum('four')).values()[0]
        district_emis_five=emis_count.aggregate(Sum('five')).values()[0]
        district_emis_six=emis_count.aggregate(Sum('six')).values()[0]
        district_emis_seven=emis_count.aggregate(Sum('seven')).values()[0]
        district_emis_eight=emis_count.aggregate(Sum('eight')).values()[0]
        district_emis_nine=emis_count.aggregate(Sum('nine')).values()[0]
        district_emis_ten=emis_count.aggregate(Sum('ten')).values()[0]
        district_emis_eleven=emis_count.aggregate(Sum('eleven')).values()[0]
        district_emis_twelve=emis_count.aggregate(Sum('twelve')).values()[0]
        district_emis_total_count=emis_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'district/district_progress_report.html',locals())


class State_level_progress_report(View):
    def get(self,request,**kwargs):
        districts=District.objects.all()
        district_ids=[]
        district_names=[]
        district_emis_one=[]
        district_emis_two=[]
        district_emis_three=[]
        district_emis_four=[]
        district_emis_five=[]
        district_emis_six=[]
        district_emis_seven=[]
        district_emis_eight=[]
        district_emis_nine=[]
        district_emis_ten=[]
        district_emis_eleven=[]
        district_emis_twelve=[]
        district_emis_total_count=[]
        for i in districts:
            district_ids.append(str(i.id))
            district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id)
            emis_count=School_child_count.objects.filter(school_id__in=school_list)
            district_emis_total_one=emis_count.aggregate(Sum('one'))
            district_emis_total_two=emis_count.aggregate(Sum('two'))
            district_emis_total_three=emis_count.aggregate(Sum('three'))
            district_emis_total_four=emis_count.aggregate(Sum('four'))
            district_emis_total_five=emis_count.aggregate(Sum('five'))
            district_emis_total_six=emis_count.aggregate(Sum('six'))
            district_emis_total_seven=emis_count.aggregate(Sum('seven'))
            district_emis_total_eight=emis_count.aggregate(Sum('eight'))
            district_emis_total_nine=emis_count.aggregate(Sum('nine'))
            district_emis_total_ten=emis_count.aggregate(Sum('ten'))
            district_emis_total_eleven=emis_count.aggregate(Sum('eleven'))
            district_emis_total_twelve=emis_count.aggregate(Sum('twelve'))
            district_emis_total_total_count=emis_count.aggregate(Sum('total_count'))
            district_emis_one+=district_emis_total_one.values()
            district_emis_two+=district_emis_total_two.values()
            district_emis_three+=district_emis_total_three.values()
            district_emis_four+=district_emis_total_four.values()
            district_emis_five+=district_emis_total_five.values()
            district_emis_six+=district_emis_total_six.values()
            district_emis_seven+=district_emis_total_seven.values()
            district_emis_eight+=district_emis_total_eight.values()
            district_emis_nine+=district_emis_total_nine.values()
            district_emis_ten+=district_emis_total_ten.values()
            district_emis_eleven+=district_emis_total_eleven.values()
            district_emis_twelve+=district_emis_total_twelve.values()
            district_emis_total_count+=district_emis_total_total_count.values()
        mylist=zip(district_ids,district_names,district_emis_one,district_emis_two,district_emis_three,district_emis_four,district_emis_five,district_emis_six,district_emis_seven,district_emis_eight,district_emis_nine,district_emis_ten,district_emis_eleven,district_emis_twelve,district_emis_total_count)
        emis_count=School_child_count.objects.all()
        state_emis_one=emis_count.aggregate(Sum('one')).values()[0]
        state_emis_two=emis_count.aggregate(Sum('two')).values()[0]
        state_emis_three=emis_count.aggregate(Sum('three')).values()[0]
        state_emis_four=emis_count.aggregate(Sum('four')).values()[0]
        state_emis_five=emis_count.aggregate(Sum('five')).values()[0]
        state_emis_six=emis_count.aggregate(Sum('six')).values()[0]
        state_emis_seven=emis_count.aggregate(Sum('seven')).values()[0]
        state_emis_eight=emis_count.aggregate(Sum('eight')).values()[0]
        state_emis_nine=emis_count.aggregate(Sum('nine')).values()[0]
        state_emis_ten=emis_count.aggregate(Sum('ten')).values()[0]
        state_emis_eleven=emis_count.aggregate(Sum('eleven')).values()[0]
        state_emis_twelve=emis_count.aggregate(Sum('twelve')).values()[0]
        state_emis_total_count=emis_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'state/state_progress_report.html',locals())



class State_level_progress_report_man_dee1(View):
    def get(self,request,**kwargs):
        dee_mis_match_ids=[7250,7249,7937,43284,7251,24041,7252,7173,7174,7175,44424,58071,7278,7280,7171,7279,7285,41949,18907,18835]
        districts=District.objects.all()
        dee_district_ids=[]
        dee_district_names=[]
        dee_district_emis_one=[]
        dee_district_emis_two=[]
        dee_district_emis_three=[]
        dee_district_emis_four=[]
        dee_district_emis_five=[]
        dee_district_emis_six=[]
        dee_district_emis_seven=[]
        dee_district_emis_eight=[]
        dee_district_emis_nine=[]
        dee_district_emis_ten=[]
        dee_district_emis_eleven=[]
        dee_district_emis_twelve=[]
        dee_district_emis_total_count=[]
        for i in districts:
            dee_district_ids.append(str(i.id))
            dee_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[1,2,3,4,5,6,8],category_id__in=[1,2,4,11])
            dee_emis_count=School_child_count.objects.filter(school_id__in=school_list).exclude(school_id__in=dee_mis_match_ids)
            dee_district_emis_total_one=dee_emis_count.aggregate(Sum('one'))
            dee_district_emis_total_two=dee_emis_count.aggregate(Sum('two'))
            dee_district_emis_total_three=dee_emis_count.aggregate(Sum('three'))
            dee_district_emis_total_four=dee_emis_count.aggregate(Sum('four'))
            dee_district_emis_total_five=dee_emis_count.aggregate(Sum('five'))
            dee_district_emis_total_six=dee_emis_count.aggregate(Sum('six'))
            dee_district_emis_total_seven=dee_emis_count.aggregate(Sum('seven'))
            dee_district_emis_total_eight=dee_emis_count.aggregate(Sum('eight'))
            dee_district_emis_total_nine=dee_emis_count.aggregate(Sum('nine'))
            dee_district_emis_total_ten=dee_emis_count.aggregate(Sum('ten'))
            dee_district_emis_total_eleven=dee_emis_count.aggregate(Sum('eleven'))
            dee_district_emis_total_twelve=dee_emis_count.aggregate(Sum('twelve'))
            dee_district_emis_total_total_count=dee_emis_count.aggregate(Sum('total_count'))
            dee_district_emis_one+=dee_district_emis_total_one.values()
            dee_district_emis_two+=dee_district_emis_total_two.values()
            dee_district_emis_three+=dee_district_emis_total_three.values()
            dee_district_emis_four+=dee_district_emis_total_four.values()
            dee_district_emis_five+=dee_district_emis_total_five.values()
            dee_district_emis_six+=dee_district_emis_total_six.values()
            dee_district_emis_seven+=dee_district_emis_total_seven.values()
            dee_district_emis_eight+=dee_district_emis_total_eight.values()
            dee_district_emis_nine+=dee_district_emis_total_nine.values()
            dee_district_emis_ten+=dee_district_emis_total_ten.values()
            dee_district_emis_eleven+=dee_district_emis_total_eleven.values()
            dee_district_emis_twelve+=dee_district_emis_total_twelve.values()
            dee_district_emis_total_count+=dee_district_emis_total_total_count.values()
        dee_mylist=zip(dee_district_ids,dee_district_names,dee_district_emis_one,dee_district_emis_two,dee_district_emis_three,dee_district_emis_four,dee_district_emis_five,dee_district_emis_six,dee_district_emis_seven,dee_district_emis_eight,dee_district_emis_nine,dee_district_emis_ten,dee_district_emis_eleven,dee_district_emis_twelve,dee_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[1,2,3,4,5,6,8],category_id__in=[1,2,4,11])
        dee_emis_count=School_child_count.objects.filter(school_id__in=school_list).exclude(school_id__in=dee_mis_match_ids)
        dee_state_emis_one=dee_emis_count.aggregate(Sum('one')).values()[0]
        dee_state_emis_two=dee_emis_count.aggregate(Sum('two')).values()[0]
        dee_state_emis_three=dee_emis_count.aggregate(Sum('three')).values()[0]
        dee_state_emis_four=dee_emis_count.aggregate(Sum('four')).values()[0]
        dee_state_emis_five=dee_emis_count.aggregate(Sum('five')).values()[0]
        dee_state_emis_six=dee_emis_count.aggregate(Sum('six')).values()[0]
        dee_state_emis_seven=dee_emis_count.aggregate(Sum('seven')).values()[0]
        dee_state_emis_eight=dee_emis_count.aggregate(Sum('eight')).values()[0]
        dee_state_emis_nine=dee_emis_count.aggregate(Sum('nine')).values()[0]
        dee_state_emis_ten=dee_emis_count.aggregate(Sum('ten')).values()[0]
        dee_state_emis_eleven=dee_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_state_emis_twelve=dee_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_state_emis_total_count=dee_emis_count.aggregate(Sum('total_count')).values()[0]
        # panchayath
        districts=District.objects.all()
        dee_pan_district_ids=[]
        dee_pan_district_names=[]
        dee_pan_district_emis_one=[]
        dee_pan_district_emis_two=[]
        dee_pan_district_emis_three=[]
        dee_pan_district_emis_four=[]
        dee_pan_district_emis_five=[]
        dee_pan_district_emis_six=[]
        dee_pan_district_emis_seven=[]
        dee_pan_district_emis_eight=[]
        dee_pan_district_emis_nine=[]
        dee_pan_district_emis_ten=[]
        dee_pan_district_emis_eleven=[]
        dee_pan_district_emis_twelve=[]
        dee_pan_district_emis_total_count=[]
        for i in districts:
            dee_pan_district_ids.append(str(i.id))
            dee_pan_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[3],category_id__in=[1,2,4])
            dee_pan_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_pan_district_emis_total_one=dee_pan_emis_count.aggregate(Sum('one'))
            dee_pan_district_emis_total_two=dee_pan_emis_count.aggregate(Sum('two'))
            dee_pan_district_emis_total_three=dee_pan_emis_count.aggregate(Sum('three'))
            dee_pan_district_emis_total_four=dee_pan_emis_count.aggregate(Sum('four'))
            dee_pan_district_emis_total_five=dee_pan_emis_count.aggregate(Sum('five'))
            dee_pan_district_emis_total_six=dee_pan_emis_count.aggregate(Sum('six'))
            dee_pan_district_emis_total_seven=dee_pan_emis_count.aggregate(Sum('seven'))
            dee_pan_district_emis_total_eight=dee_pan_emis_count.aggregate(Sum('eight'))
            dee_pan_district_emis_total_nine=dee_pan_emis_count.aggregate(Sum('nine'))
            dee_pan_district_emis_total_ten=dee_pan_emis_count.aggregate(Sum('ten'))
            dee_pan_district_emis_total_eleven=dee_pan_emis_count.aggregate(Sum('eleven'))
            dee_pan_district_emis_total_twelve=dee_pan_emis_count.aggregate(Sum('twelve'))
            dee_pan_district_emis_total_total_count=dee_pan_emis_count.aggregate(Sum('total_count'))
            dee_pan_district_emis_one+=dee_pan_district_emis_total_one.values()
            dee_pan_district_emis_two+=dee_pan_district_emis_total_two.values()
            dee_pan_district_emis_three+=dee_pan_district_emis_total_three.values()
            dee_pan_district_emis_four+=dee_pan_district_emis_total_four.values()
            dee_pan_district_emis_five+=dee_pan_district_emis_total_five.values()
            dee_pan_district_emis_six+=dee_pan_district_emis_total_six.values()
            dee_pan_district_emis_seven+=dee_pan_district_emis_total_seven.values()
            dee_pan_district_emis_eight+=dee_pan_district_emis_total_eight.values()
            dee_pan_district_emis_nine+=dee_pan_district_emis_total_nine.values()
            dee_pan_district_emis_ten+=dee_pan_district_emis_total_ten.values()
            dee_pan_district_emis_eleven+=dee_pan_district_emis_total_eleven.values()
            dee_pan_district_emis_twelve+=dee_pan_district_emis_total_twelve.values()
            dee_pan_district_emis_total_count+=dee_pan_district_emis_total_total_count.values()
        dee_pan_mylist=zip(dee_pan_district_ids,dee_pan_district_names,dee_pan_district_emis_one,dee_pan_district_emis_two,dee_pan_district_emis_three,dee_pan_district_emis_four,dee_pan_district_emis_five,dee_pan_district_emis_six,dee_pan_district_emis_seven,dee_pan_district_emis_eight,dee_pan_district_emis_nine,dee_pan_district_emis_ten,dee_pan_district_emis_eleven,dee_pan_district_emis_twelve,dee_pan_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[3],category_id__in=[1,2,4])
        dee_pan_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_pan_state_emis_one=dee_pan_emis_count.aggregate(Sum('one')).values()[0]
        dee_pan_state_emis_two=dee_pan_emis_count.aggregate(Sum('two')).values()[0]
        dee_pan_state_emis_three=dee_pan_emis_count.aggregate(Sum('three')).values()[0]
        dee_pan_state_emis_four=dee_pan_emis_count.aggregate(Sum('four')).values()[0]
        dee_pan_state_emis_five=dee_pan_emis_count.aggregate(Sum('five')).values()[0]
        dee_pan_state_emis_six=dee_pan_emis_count.aggregate(Sum('six')).values()[0]
        dee_pan_state_emis_seven=dee_pan_emis_count.aggregate(Sum('seven')).values()[0]
        dee_pan_state_emis_eight=dee_pan_emis_count.aggregate(Sum('eight')).values()[0]
        dee_pan_state_emis_nine=dee_pan_emis_count.aggregate(Sum('nine')).values()[0]
        dee_pan_state_emis_ten=dee_pan_emis_count.aggregate(Sum('ten')).values()[0]
        dee_pan_state_emis_eleven=dee_pan_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_pan_state_emis_twelve=dee_pan_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_pan_state_emis_total_count=dee_pan_emis_count.aggregate(Sum('total_count')).values()[0]
        # municipal
        dee_mpl_district_ids=[]
        dee_mpl_district_names=[]
        dee_mpl_district_emis_one=[]
        dee_mpl_district_emis_two=[]
        dee_mpl_district_emis_three=[]
        dee_mpl_district_emis_four=[]
        dee_mpl_district_emis_five=[]
        dee_mpl_district_emis_six=[]
        dee_mpl_district_emis_seven=[]
        dee_mpl_district_emis_eight=[]
        dee_mpl_district_emis_nine=[]
        dee_mpl_district_emis_ten=[]
        dee_mpl_district_emis_eleven=[]
        dee_mpl_district_emis_twelve=[]
        dee_mpl_district_emis_total_count=[]
        for i in districts:
            dee_mpl_district_ids.append(str(i.id))
            dee_mpl_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[5],category_id__in=[1,2,4])
            dee_mpl_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_mpl_district_emis_total_one=dee_mpl_emis_count.aggregate(Sum('one'))
            dee_mpl_district_emis_total_two=dee_mpl_emis_count.aggregate(Sum('two'))
            dee_mpl_district_emis_total_three=dee_mpl_emis_count.aggregate(Sum('three'))
            dee_mpl_district_emis_total_four=dee_mpl_emis_count.aggregate(Sum('four'))
            dee_mpl_district_emis_total_five=dee_mpl_emis_count.aggregate(Sum('five'))
            dee_mpl_district_emis_total_six=dee_mpl_emis_count.aggregate(Sum('six'))
            dee_mpl_district_emis_total_seven=dee_mpl_emis_count.aggregate(Sum('seven'))
            dee_mpl_district_emis_total_eight=dee_mpl_emis_count.aggregate(Sum('eight'))
            dee_mpl_district_emis_total_nine=dee_mpl_emis_count.aggregate(Sum('nine'))
            dee_mpl_district_emis_total_ten=dee_mpl_emis_count.aggregate(Sum('ten'))
            dee_mpl_district_emis_total_eleven=dee_mpl_emis_count.aggregate(Sum('eleven'))
            dee_mpl_district_emis_total_twelve=dee_mpl_emis_count.aggregate(Sum('twelve'))
            dee_mpl_district_emis_total_total_count=dee_mpl_emis_count.aggregate(Sum('total_count'))
            dee_mpl_district_emis_one+=dee_mpl_district_emis_total_one.values()
            dee_mpl_district_emis_two+=dee_mpl_district_emis_total_two.values()
            dee_mpl_district_emis_three+=dee_mpl_district_emis_total_three.values()
            dee_mpl_district_emis_four+=dee_mpl_district_emis_total_four.values()
            dee_mpl_district_emis_five+=dee_mpl_district_emis_total_five.values()
            dee_mpl_district_emis_six+=dee_mpl_district_emis_total_six.values()
            dee_mpl_district_emis_seven+=dee_mpl_district_emis_total_seven.values()
            dee_mpl_district_emis_eight+=dee_mpl_district_emis_total_eight.values()
            dee_mpl_district_emis_nine+=dee_mpl_district_emis_total_nine.values()
            dee_mpl_district_emis_ten+=dee_mpl_district_emis_total_ten.values()
            dee_mpl_district_emis_eleven+=dee_mpl_district_emis_total_eleven.values()
            dee_mpl_district_emis_twelve+=dee_mpl_district_emis_total_twelve.values()
            dee_mpl_district_emis_total_count+=dee_mpl_district_emis_total_total_count.values()
        dee_mpl_mylist=zip(dee_mpl_district_ids,dee_mpl_district_names,dee_mpl_district_emis_one,dee_mpl_district_emis_two,dee_mpl_district_emis_three,dee_mpl_district_emis_four,dee_mpl_district_emis_five,dee_mpl_district_emis_six,dee_mpl_district_emis_seven,dee_mpl_district_emis_eight,dee_mpl_district_emis_nine,dee_mpl_district_emis_ten,dee_mpl_district_emis_eleven,dee_mpl_district_emis_twelve,dee_mpl_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[5],category_id__in=[1,2,4])
        dee_mpl_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_mpl_state_emis_one=dee_mpl_emis_count.aggregate(Sum('one')).values()[0]
        dee_mpl_state_emis_two=dee_mpl_emis_count.aggregate(Sum('two')).values()[0]
        dee_mpl_state_emis_three=dee_mpl_emis_count.aggregate(Sum('three')).values()[0]
        dee_mpl_state_emis_four=dee_mpl_emis_count.aggregate(Sum('four')).values()[0]
        dee_mpl_state_emis_five=dee_mpl_emis_count.aggregate(Sum('five')).values()[0]
        dee_mpl_state_emis_six=dee_mpl_emis_count.aggregate(Sum('six')).values()[0]
        dee_mpl_state_emis_seven=dee_mpl_emis_count.aggregate(Sum('seven')).values()[0]
        dee_mpl_state_emis_eight=dee_mpl_emis_count.aggregate(Sum('eight')).values()[0]
        dee_mpl_state_emis_nine=dee_mpl_emis_count.aggregate(Sum('nine')).values()[0]
        dee_mpl_state_emis_ten=dee_mpl_emis_count.aggregate(Sum('ten')).values()[0]
        dee_mpl_state_emis_eleven=dee_mpl_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_mpl_state_emis_twelve=dee_mpl_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_mpl_state_emis_total_count=dee_mpl_emis_count.aggregate(Sum('total_count')).values()[0]
        # Aided
        dee_aid_district_ids=[]
        dee_aid_district_names=[]
        dee_aid_district_emis_one=[]
        dee_aid_district_emis_two=[]
        dee_aid_district_emis_three=[]
        dee_aid_district_emis_four=[]
        dee_aid_district_emis_five=[]
        dee_aid_district_emis_six=[]
        dee_aid_district_emis_seven=[]
        dee_aid_district_emis_eight=[]
        dee_aid_district_emis_nine=[]
        dee_aid_district_emis_ten=[]
        dee_aid_district_emis_eleven=[]
        dee_aid_district_emis_twelve=[]
        dee_aid_district_emis_total_count=[]
        for i in districts:
            dee_aid_district_ids.append(str(i.id))
            dee_aid_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[6],category_id__in=[1,2,4])
            dee_aid_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_aid_district_emis_total_one=dee_aid_emis_count.aggregate(Sum('one'))
            dee_aid_district_emis_total_two=dee_aid_emis_count.aggregate(Sum('two'))
            dee_aid_district_emis_total_three=dee_aid_emis_count.aggregate(Sum('three'))
            dee_aid_district_emis_total_four=dee_aid_emis_count.aggregate(Sum('four'))
            dee_aid_district_emis_total_five=dee_aid_emis_count.aggregate(Sum('five'))
            dee_aid_district_emis_total_six=dee_aid_emis_count.aggregate(Sum('six'))
            dee_aid_district_emis_total_seven=dee_aid_emis_count.aggregate(Sum('seven'))
            dee_aid_district_emis_total_eight=dee_aid_emis_count.aggregate(Sum('eight'))
            dee_aid_district_emis_total_nine=dee_aid_emis_count.aggregate(Sum('nine'))
            dee_aid_district_emis_total_ten=dee_aid_emis_count.aggregate(Sum('ten'))
            dee_aid_district_emis_total_eleven=dee_aid_emis_count.aggregate(Sum('eleven'))
            dee_aid_district_emis_total_twelve=dee_aid_emis_count.aggregate(Sum('twelve'))
            dee_aid_district_emis_total_total_count=dee_aid_emis_count.aggregate(Sum('total_count'))
            dee_aid_district_emis_one+=dee_aid_district_emis_total_one.values()
            dee_aid_district_emis_two+=dee_aid_district_emis_total_two.values()
            dee_aid_district_emis_three+=dee_aid_district_emis_total_three.values()
            dee_aid_district_emis_four+=dee_aid_district_emis_total_four.values()
            dee_aid_district_emis_five+=dee_aid_district_emis_total_five.values()
            dee_aid_district_emis_six+=dee_aid_district_emis_total_six.values()
            dee_aid_district_emis_seven+=dee_aid_district_emis_total_seven.values()
            dee_aid_district_emis_eight+=dee_aid_district_emis_total_eight.values()
            dee_aid_district_emis_nine+=dee_aid_district_emis_total_nine.values()
            dee_aid_district_emis_ten+=dee_aid_district_emis_total_ten.values()
            dee_aid_district_emis_eleven+=dee_aid_district_emis_total_eleven.values()
            dee_aid_district_emis_twelve+=dee_aid_district_emis_total_twelve.values()
            dee_aid_district_emis_total_count+=dee_aid_district_emis_total_total_count.values()
        dee_aid_mylist=zip(dee_aid_district_ids,dee_aid_district_names,dee_aid_district_emis_one,dee_aid_district_emis_two,dee_aid_district_emis_three,dee_aid_district_emis_four,dee_aid_district_emis_five,dee_aid_district_emis_six,dee_aid_district_emis_seven,dee_aid_district_emis_eight,dee_aid_district_emis_nine,dee_aid_district_emis_ten,dee_aid_district_emis_eleven,dee_aid_district_emis_twelve,dee_aid_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[6],category_id__in=[1,2,4])
        dee_aid_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_aid_state_emis_one=dee_aid_emis_count.aggregate(Sum('one')).values()[0]
        dee_aid_state_emis_two=dee_aid_emis_count.aggregate(Sum('two')).values()[0]
        dee_aid_state_emis_three=dee_aid_emis_count.aggregate(Sum('three')).values()[0]
        dee_aid_state_emis_four=dee_aid_emis_count.aggregate(Sum('four')).values()[0]
        dee_aid_state_emis_five=dee_aid_emis_count.aggregate(Sum('five')).values()[0]
        dee_aid_state_emis_six=dee_aid_emis_count.aggregate(Sum('six')).values()[0]
        dee_aid_state_emis_seven=dee_aid_emis_count.aggregate(Sum('seven')).values()[0]
        dee_aid_state_emis_eight=dee_aid_emis_count.aggregate(Sum('eight')).values()[0]
        dee_aid_state_emis_nine=dee_aid_emis_count.aggregate(Sum('nine')).values()[0]
        dee_aid_state_emis_ten=dee_aid_emis_count.aggregate(Sum('ten')).values()[0]
        dee_aid_state_emis_eleven=dee_aid_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_aid_state_emis_twelve=dee_aid_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_aid_state_emis_total_count=dee_aid_emis_count.aggregate(Sum('total_count')).values()[0]
        # Nursery
        dee_nur_district_ids=[]
        dee_nur_district_names=[]
        dee_nur_district_emis_one=[]
        dee_nur_district_emis_two=[]
        dee_nur_district_emis_three=[]
        dee_nur_district_emis_four=[]
        dee_nur_district_emis_five=[]
        dee_nur_district_emis_six=[]
        dee_nur_district_emis_seven=[]
        dee_nur_district_emis_eight=[]
        dee_nur_district_emis_nine=[]
        dee_nur_district_emis_ten=[]
        dee_nur_district_emis_eleven=[]
        dee_nur_district_emis_twelve=[]
        dee_nur_district_emis_total_count=[]
        for i in districts:
            dee_nur_district_ids.append(str(i.id))
            dee_nur_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[8],category_id__in=[11])
            dee_nur_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_nur_district_emis_total_one=dee_nur_emis_count.aggregate(Sum('one'))
            dee_nur_district_emis_total_two=dee_nur_emis_count.aggregate(Sum('two'))
            dee_nur_district_emis_total_three=dee_nur_emis_count.aggregate(Sum('three'))
            dee_nur_district_emis_total_four=dee_nur_emis_count.aggregate(Sum('four'))
            dee_nur_district_emis_total_five=dee_nur_emis_count.aggregate(Sum('five'))
            dee_nur_district_emis_total_six=dee_nur_emis_count.aggregate(Sum('six'))
            dee_nur_district_emis_total_seven=dee_nur_emis_count.aggregate(Sum('seven'))
            dee_nur_district_emis_total_eight=dee_nur_emis_count.aggregate(Sum('eight'))
            dee_nur_district_emis_total_nine=dee_nur_emis_count.aggregate(Sum('nine'))
            dee_nur_district_emis_total_ten=dee_nur_emis_count.aggregate(Sum('ten'))
            dee_nur_district_emis_total_eleven=dee_nur_emis_count.aggregate(Sum('eleven'))
            dee_nur_district_emis_total_twelve=dee_nur_emis_count.aggregate(Sum('twelve'))
            dee_nur_district_emis_total_total_count=dee_nur_emis_count.aggregate(Sum('total_count'))
            dee_nur_district_emis_one+=dee_nur_district_emis_total_one.values()
            dee_nur_district_emis_two+=dee_nur_district_emis_total_two.values()
            dee_nur_district_emis_three+=dee_nur_district_emis_total_three.values()
            dee_nur_district_emis_four+=dee_nur_district_emis_total_four.values()
            dee_nur_district_emis_five+=dee_nur_district_emis_total_five.values()
            dee_nur_district_emis_six+=dee_nur_district_emis_total_six.values()
            dee_nur_district_emis_seven+=dee_nur_district_emis_total_seven.values()
            dee_nur_district_emis_eight+=dee_nur_district_emis_total_eight.values()
            dee_nur_district_emis_nine+=dee_nur_district_emis_total_nine.values()
            dee_nur_district_emis_ten+=dee_nur_district_emis_total_ten.values()
            dee_nur_district_emis_eleven+=dee_nur_district_emis_total_eleven.values()
            dee_nur_district_emis_twelve+=dee_nur_district_emis_total_twelve.values()
            dee_nur_district_emis_total_count+=dee_nur_district_emis_total_total_count.values()
        dee_nur_mylist=zip(dee_nur_district_ids,dee_nur_district_names,dee_nur_district_emis_one,dee_nur_district_emis_two,dee_nur_district_emis_three,dee_nur_district_emis_four,dee_nur_district_emis_five,dee_nur_district_emis_six,dee_nur_district_emis_seven,dee_nur_district_emis_eight,dee_nur_district_emis_nine,dee_nur_district_emis_ten,dee_nur_district_emis_eleven,dee_nur_district_emis_twelve,dee_nur_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[8],category_id__in=[11])
        dee_nur_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_nur_state_emis_one=dee_nur_emis_count.aggregate(Sum('one')).values()[0]
        dee_nur_state_emis_two=dee_nur_emis_count.aggregate(Sum('two')).values()[0]
        dee_nur_state_emis_three=dee_nur_emis_count.aggregate(Sum('three')).values()[0]
        dee_nur_state_emis_four=dee_nur_emis_count.aggregate(Sum('four')).values()[0]
        dee_nur_state_emis_five=dee_nur_emis_count.aggregate(Sum('five')).values()[0]
        dee_nur_state_emis_six=dee_nur_emis_count.aggregate(Sum('six')).values()[0]
        dee_nur_state_emis_seven=dee_nur_emis_count.aggregate(Sum('seven')).values()[0]
        dee_nur_state_emis_eight=dee_nur_emis_count.aggregate(Sum('eight')).values()[0]
        dee_nur_state_emis_nine=dee_nur_emis_count.aggregate(Sum('nine')).values()[0]
        dee_nur_state_emis_ten=dee_nur_emis_count.aggregate(Sum('ten')).values()[0]
        dee_nur_state_emis_eleven=dee_nur_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_nur_state_emis_twelve=dee_nur_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_nur_state_emis_total_count=dee_nur_emis_count.aggregate(Sum('total_count')).values()[0]
        # pvt aided
        dee_pvt_district_ids=[]
        dee_pvt_district_names=[]
        dee_pvt_district_emis_one=[]
        dee_pvt_district_emis_two=[]
        dee_pvt_district_emis_three=[]
        dee_pvt_district_emis_four=[]
        dee_pvt_district_emis_five=[]
        dee_pvt_district_emis_six=[]
        dee_pvt_district_emis_seven=[]
        dee_pvt_district_emis_eight=[]
        dee_pvt_district_emis_nine=[]
        dee_pvt_district_emis_ten=[]
        dee_pvt_district_emis_eleven=[]
        dee_pvt_district_emis_twelve=[]
        dee_pvt_district_emis_total_count=[]
        for i in districts:
            dee_pvt_district_ids.append(str(i.id))
            dee_pvt_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[8],category_id__in=[1,2,4])
            dee_pvt_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_pvt_district_emis_total_one=dee_pvt_emis_count.aggregate(Sum('one'))
            dee_pvt_district_emis_total_two=dee_pvt_emis_count.aggregate(Sum('two'))
            dee_pvt_district_emis_total_three=dee_pvt_emis_count.aggregate(Sum('three'))
            dee_pvt_district_emis_total_four=dee_pvt_emis_count.aggregate(Sum('four'))
            dee_pvt_district_emis_total_five=dee_pvt_emis_count.aggregate(Sum('five'))
            dee_pvt_district_emis_total_six=dee_pvt_emis_count.aggregate(Sum('six'))
            dee_pvt_district_emis_total_seven=dee_pvt_emis_count.aggregate(Sum('seven'))
            dee_pvt_district_emis_total_eight=dee_pvt_emis_count.aggregate(Sum('eight'))
            dee_pvt_district_emis_total_nine=dee_pvt_emis_count.aggregate(Sum('nine'))
            dee_pvt_district_emis_total_ten=dee_pvt_emis_count.aggregate(Sum('ten'))
            dee_pvt_district_emis_total_eleven=dee_pvt_emis_count.aggregate(Sum('eleven'))
            dee_pvt_district_emis_total_twelve=dee_pvt_emis_count.aggregate(Sum('twelve'))
            dee_pvt_district_emis_total_total_count=dee_pvt_emis_count.aggregate(Sum('total_count'))
            dee_pvt_district_emis_one+=dee_pvt_district_emis_total_one.values()
            dee_pvt_district_emis_two+=dee_pvt_district_emis_total_two.values()
            dee_pvt_district_emis_three+=dee_pvt_district_emis_total_three.values()
            dee_pvt_district_emis_four+=dee_pvt_district_emis_total_four.values()
            dee_pvt_district_emis_five+=dee_pvt_district_emis_total_five.values()
            dee_pvt_district_emis_six+=dee_pvt_district_emis_total_six.values()
            dee_pvt_district_emis_seven+=dee_pvt_district_emis_total_seven.values()
            dee_pvt_district_emis_eight+=dee_pvt_district_emis_total_eight.values()
            dee_pvt_district_emis_nine+=dee_pvt_district_emis_total_nine.values()
            dee_pvt_district_emis_ten+=dee_pvt_district_emis_total_ten.values()
            dee_pvt_district_emis_eleven+=dee_pvt_district_emis_total_eleven.values()
            dee_pvt_district_emis_twelve+=dee_pvt_district_emis_total_twelve.values()
            dee_pvt_district_emis_total_count+=dee_pvt_district_emis_total_total_count.values()
        dee_pvt_mylist=zip(dee_pvt_district_ids,dee_pvt_district_names,dee_pvt_district_emis_one,dee_pvt_district_emis_two,dee_pvt_district_emis_three,dee_pvt_district_emis_four,dee_pvt_district_emis_five,dee_pvt_district_emis_six,dee_pvt_district_emis_seven,dee_pvt_district_emis_eight,dee_pvt_district_emis_nine,dee_pvt_district_emis_ten,dee_pvt_district_emis_eleven,dee_pvt_district_emis_twelve,dee_pvt_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[8],category_id__in=[1,2,4])
        dee_pvt_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_pvt_state_emis_one=dee_pvt_emis_count.aggregate(Sum('one')).values()[0]
        dee_pvt_state_emis_two=dee_pvt_emis_count.aggregate(Sum('two')).values()[0]
        dee_pvt_state_emis_three=dee_pvt_emis_count.aggregate(Sum('three')).values()[0]
        dee_pvt_state_emis_four=dee_pvt_emis_count.aggregate(Sum('four')).values()[0]
        dee_pvt_state_emis_five=dee_pvt_emis_count.aggregate(Sum('five')).values()[0]
        dee_pvt_state_emis_six=dee_pvt_emis_count.aggregate(Sum('six')).values()[0]
        dee_pvt_state_emis_seven=dee_pvt_emis_count.aggregate(Sum('seven')).values()[0]
        dee_pvt_state_emis_eight=dee_pvt_emis_count.aggregate(Sum('eight')).values()[0]
        dee_pvt_state_emis_nine=dee_pvt_emis_count.aggregate(Sum('nine')).values()[0]
        dee_pvt_state_emis_ten=dee_pvt_emis_count.aggregate(Sum('ten')).values()[0]
        dee_pvt_state_emis_eleven=dee_pvt_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_pvt_state_emis_twelve=dee_pvt_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_pvt_state_emis_total_count=dee_pvt_emis_count.aggregate(Sum('total_count')).values()[0]
        # corporation
        dee_cor_district_ids=[]
        dee_cor_district_names=[]
        dee_cor_district_emis_one=[]
        dee_cor_district_emis_two=[]
        dee_cor_district_emis_three=[]
        dee_cor_district_emis_four=[]
        dee_cor_district_emis_five=[]
        dee_cor_district_emis_six=[]
        dee_cor_district_emis_seven=[]
        dee_cor_district_emis_eight=[]
        dee_cor_district_emis_nine=[]
        dee_cor_district_emis_ten=[]
        dee_cor_district_emis_eleven=[]
        dee_cor_district_emis_twelve=[]
        dee_cor_district_emis_total_count=[]
        for i in districts:
            dee_cor_district_ids.append(str(i.id))
            dee_cor_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[4],category_id__in=[1,2,4])
            dee_cor_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_cor_district_emis_total_one=dee_cor_emis_count.aggregate(Sum('one'))
            dee_cor_district_emis_total_two=dee_cor_emis_count.aggregate(Sum('two'))
            dee_cor_district_emis_total_three=dee_cor_emis_count.aggregate(Sum('three'))
            dee_cor_district_emis_total_four=dee_cor_emis_count.aggregate(Sum('four'))
            dee_cor_district_emis_total_five=dee_cor_emis_count.aggregate(Sum('five'))
            dee_cor_district_emis_total_six=dee_cor_emis_count.aggregate(Sum('six'))
            dee_cor_district_emis_total_seven=dee_cor_emis_count.aggregate(Sum('seven'))
            dee_cor_district_emis_total_eight=dee_cor_emis_count.aggregate(Sum('eight'))
            dee_cor_district_emis_total_nine=dee_cor_emis_count.aggregate(Sum('nine'))
            dee_cor_district_emis_total_ten=dee_cor_emis_count.aggregate(Sum('ten'))
            dee_cor_district_emis_total_eleven=dee_cor_emis_count.aggregate(Sum('eleven'))
            dee_cor_district_emis_total_twelve=dee_cor_emis_count.aggregate(Sum('twelve'))
            dee_cor_district_emis_total_total_count=dee_cor_emis_count.aggregate(Sum('total_count'))
            dee_cor_district_emis_one+=dee_cor_district_emis_total_one.values()
            dee_cor_district_emis_two+=dee_cor_district_emis_total_two.values()
            dee_cor_district_emis_three+=dee_cor_district_emis_total_three.values()
            dee_cor_district_emis_four+=dee_cor_district_emis_total_four.values()
            dee_cor_district_emis_five+=dee_cor_district_emis_total_five.values()
            dee_cor_district_emis_six+=dee_cor_district_emis_total_six.values()
            dee_cor_district_emis_seven+=dee_cor_district_emis_total_seven.values()
            dee_cor_district_emis_eight+=dee_cor_district_emis_total_eight.values()
            dee_cor_district_emis_nine+=dee_cor_district_emis_total_nine.values()
            dee_cor_district_emis_ten+=dee_cor_district_emis_total_ten.values()
            dee_cor_district_emis_eleven+=dee_cor_district_emis_total_eleven.values()
            dee_cor_district_emis_twelve+=dee_cor_district_emis_total_twelve.values()
            dee_cor_district_emis_total_count+=dee_cor_district_emis_total_total_count.values()
        dee_cor_mylist=zip(dee_cor_district_ids,dee_cor_district_names,dee_cor_district_emis_one,dee_cor_district_emis_two,dee_cor_district_emis_three,dee_cor_district_emis_four,dee_cor_district_emis_five,dee_cor_district_emis_six,dee_cor_district_emis_seven,dee_cor_district_emis_eight,dee_cor_district_emis_nine,dee_cor_district_emis_ten,dee_cor_district_emis_eleven,dee_cor_district_emis_twelve,dee_cor_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[4],category_id__in=[1,2,4])
        dee_cor_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_cor_state_emis_one=dee_cor_emis_count.aggregate(Sum('one')).values()[0]
        dee_cor_state_emis_two=dee_cor_emis_count.aggregate(Sum('two')).values()[0]
        dee_cor_state_emis_three=dee_cor_emis_count.aggregate(Sum('three')).values()[0]
        dee_cor_state_emis_four=dee_cor_emis_count.aggregate(Sum('four')).values()[0]
        dee_cor_state_emis_five=dee_cor_emis_count.aggregate(Sum('five')).values()[0]
        dee_cor_state_emis_six=dee_cor_emis_count.aggregate(Sum('six')).values()[0]
        dee_cor_state_emis_seven=dee_cor_emis_count.aggregate(Sum('seven')).values()[0]
        dee_cor_state_emis_eight=dee_cor_emis_count.aggregate(Sum('eight')).values()[0]
        dee_cor_state_emis_nine=dee_cor_emis_count.aggregate(Sum('nine')).values()[0]
        dee_cor_state_emis_ten=dee_cor_emis_count.aggregate(Sum('ten')).values()[0]
        dee_cor_state_emis_eleven=dee_cor_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_cor_state_emis_twelve=dee_cor_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_cor_state_emis_total_count=dee_cor_emis_count.aggregate(Sum('total_count')).values()[0]
        # adw
        dee_adw_district_ids=[]
        dee_adw_district_names=[]
        dee_adw_district_emis_one=[]
        dee_adw_district_emis_two=[]
        dee_adw_district_emis_three=[]
        dee_adw_district_emis_four=[]
        dee_adw_district_emis_five=[]
        dee_adw_district_emis_six=[]
        dee_adw_district_emis_seven=[]
        dee_adw_district_emis_eight=[]
        dee_adw_district_emis_nine=[]
        dee_adw_district_emis_ten=[]
        dee_adw_district_emis_eleven=[]
        dee_adw_district_emis_twelve=[]
        dee_adw_district_emis_total_count=[]
        for i in districts:
            dee_adw_district_ids.append(str(i.id))
            dee_adw_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[2],category_id__in=[1,2,4])
            dee_adw_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_adw_district_emis_total_one=dee_adw_emis_count.aggregate(Sum('one'))
            dee_adw_district_emis_total_two=dee_adw_emis_count.aggregate(Sum('two'))
            dee_adw_district_emis_total_three=dee_adw_emis_count.aggregate(Sum('three'))
            dee_adw_district_emis_total_four=dee_adw_emis_count.aggregate(Sum('four'))
            dee_adw_district_emis_total_five=dee_adw_emis_count.aggregate(Sum('five'))
            dee_adw_district_emis_total_six=dee_adw_emis_count.aggregate(Sum('six'))
            dee_adw_district_emis_total_seven=dee_adw_emis_count.aggregate(Sum('seven'))
            dee_adw_district_emis_total_eight=dee_adw_emis_count.aggregate(Sum('eight'))
            dee_adw_district_emis_total_nine=dee_adw_emis_count.aggregate(Sum('nine'))
            dee_adw_district_emis_total_ten=dee_adw_emis_count.aggregate(Sum('ten'))
            dee_adw_district_emis_total_eleven=dee_adw_emis_count.aggregate(Sum('eleven'))
            dee_adw_district_emis_total_twelve=dee_adw_emis_count.aggregate(Sum('twelve'))
            dee_adw_district_emis_total_total_count=dee_adw_emis_count.aggregate(Sum('total_count'))
            dee_adw_district_emis_one+=dee_adw_district_emis_total_one.values()
            dee_adw_district_emis_two+=dee_adw_district_emis_total_two.values()
            dee_adw_district_emis_three+=dee_adw_district_emis_total_three.values()
            dee_adw_district_emis_four+=dee_adw_district_emis_total_four.values()
            dee_adw_district_emis_five+=dee_adw_district_emis_total_five.values()
            dee_adw_district_emis_six+=dee_adw_district_emis_total_six.values()
            dee_adw_district_emis_seven+=dee_adw_district_emis_total_seven.values()
            dee_adw_district_emis_eight+=dee_adw_district_emis_total_eight.values()
            dee_adw_district_emis_nine+=dee_adw_district_emis_total_nine.values()
            dee_adw_district_emis_ten+=dee_adw_district_emis_total_ten.values()
            dee_adw_district_emis_eleven+=dee_adw_district_emis_total_eleven.values()
            dee_adw_district_emis_twelve+=dee_adw_district_emis_total_twelve.values()
            dee_adw_district_emis_total_count+=dee_adw_district_emis_total_total_count.values()
        dee_adw_mylist=zip(dee_adw_district_ids,dee_adw_district_names,dee_adw_district_emis_one,dee_adw_district_emis_two,dee_adw_district_emis_three,dee_adw_district_emis_four,dee_adw_district_emis_five,dee_adw_district_emis_six,dee_adw_district_emis_seven,dee_adw_district_emis_eight,dee_adw_district_emis_nine,dee_adw_district_emis_ten,dee_adw_district_emis_eleven,dee_adw_district_emis_twelve,dee_adw_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[2],category_id__in=[1,2,4])
        dee_adw_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_adw_state_emis_one=dee_adw_emis_count.aggregate(Sum('one')).values()[0]
        dee_adw_state_emis_two=dee_adw_emis_count.aggregate(Sum('two')).values()[0]
        dee_adw_state_emis_three=dee_adw_emis_count.aggregate(Sum('three')).values()[0]
        dee_adw_state_emis_four=dee_adw_emis_count.aggregate(Sum('four')).values()[0]
        dee_adw_state_emis_five=dee_adw_emis_count.aggregate(Sum('five')).values()[0]
        dee_adw_state_emis_six=dee_adw_emis_count.aggregate(Sum('six')).values()[0]
        dee_adw_state_emis_seven=dee_adw_emis_count.aggregate(Sum('seven')).values()[0]
        dee_adw_state_emis_eight=dee_adw_emis_count.aggregate(Sum('eight')).values()[0]
        dee_adw_state_emis_nine=dee_adw_emis_count.aggregate(Sum('nine')).values()[0]
        dee_adw_state_emis_ten=dee_adw_emis_count.aggregate(Sum('ten')).values()[0]
        dee_adw_state_emis_eleven=dee_adw_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_adw_state_emis_twelve=dee_adw_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_adw_state_emis_total_count=dee_adw_emis_count.aggregate(Sum('total_count')).values()[0]
        # gov
        dee_gov_district_ids=[]
        dee_gov_district_names=[]
        dee_gov_district_emis_one=[]
        dee_gov_district_emis_two=[]
        dee_gov_district_emis_three=[]
        dee_gov_district_emis_four=[]
        dee_gov_district_emis_five=[]
        dee_gov_district_emis_six=[]
        dee_gov_district_emis_seven=[]
        dee_gov_district_emis_eight=[]
        dee_gov_district_emis_nine=[]
        dee_gov_district_emis_ten=[]
        dee_gov_district_emis_eleven=[]
        dee_gov_district_emis_twelve=[]
        dee_gov_district_emis_total_count=[]
        for i in districts:
            dee_gov_district_ids.append(str(i.id))
            dee_gov_district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id,management_id__in=[1],category_id__in=[1,2,4])
            dee_gov_emis_count=School_child_count.objects.filter(school_id__in=school_list)
            dee_gov_district_emis_total_one=dee_gov_emis_count.aggregate(Sum('one'))
            dee_gov_district_emis_total_two=dee_gov_emis_count.aggregate(Sum('two'))
            dee_gov_district_emis_total_three=dee_gov_emis_count.aggregate(Sum('three'))
            dee_gov_district_emis_total_four=dee_gov_emis_count.aggregate(Sum('four'))
            dee_gov_district_emis_total_five=dee_gov_emis_count.aggregate(Sum('five'))
            dee_gov_district_emis_total_six=dee_gov_emis_count.aggregate(Sum('six'))
            dee_gov_district_emis_total_seven=dee_gov_emis_count.aggregate(Sum('seven'))
            dee_gov_district_emis_total_eight=dee_gov_emis_count.aggregate(Sum('eight'))
            dee_gov_district_emis_total_nine=dee_gov_emis_count.aggregate(Sum('nine'))
            dee_gov_district_emis_total_ten=dee_gov_emis_count.aggregate(Sum('ten'))
            dee_gov_district_emis_total_eleven=dee_gov_emis_count.aggregate(Sum('eleven'))
            dee_gov_district_emis_total_twelve=dee_gov_emis_count.aggregate(Sum('twelve'))
            dee_gov_district_emis_total_total_count=dee_gov_emis_count.aggregate(Sum('total_count'))
            dee_gov_district_emis_one+=dee_gov_district_emis_total_one.values()
            dee_gov_district_emis_two+=dee_gov_district_emis_total_two.values()
            dee_gov_district_emis_three+=dee_gov_district_emis_total_three.values()
            dee_gov_district_emis_four+=dee_gov_district_emis_total_four.values()
            dee_gov_district_emis_five+=dee_gov_district_emis_total_five.values()
            dee_gov_district_emis_six+=dee_gov_district_emis_total_six.values()
            dee_gov_district_emis_seven+=dee_gov_district_emis_total_seven.values()
            dee_gov_district_emis_eight+=dee_gov_district_emis_total_eight.values()
            dee_gov_district_emis_nine+=dee_gov_district_emis_total_nine.values()
            dee_gov_district_emis_ten+=dee_gov_district_emis_total_ten.values()
            dee_gov_district_emis_eleven+=dee_gov_district_emis_total_eleven.values()
            dee_gov_district_emis_twelve+=dee_gov_district_emis_total_twelve.values()
            dee_gov_district_emis_total_count+=dee_gov_district_emis_total_total_count.values()
        dee_gov_mylist=zip(dee_gov_district_ids,dee_gov_district_names,dee_gov_district_emis_one,dee_gov_district_emis_two,dee_gov_district_emis_three,dee_gov_district_emis_four,dee_gov_district_emis_five,dee_gov_district_emis_six,dee_gov_district_emis_seven,dee_gov_district_emis_eight,dee_gov_district_emis_nine,dee_gov_district_emis_ten,dee_gov_district_emis_eleven,dee_gov_district_emis_twelve,dee_gov_district_emis_total_count)
        school_list=School.objects.filter(management_id__in=[1],category_id__in=[1,2,4])
        dee_gov_emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dee_gov_state_emis_one=dee_gov_emis_count.aggregate(Sum('one')).values()[0]
        dee_gov_state_emis_two=dee_gov_emis_count.aggregate(Sum('two')).values()[0]
        dee_gov_state_emis_three=dee_gov_emis_count.aggregate(Sum('three')).values()[0]
        dee_gov_state_emis_four=dee_gov_emis_count.aggregate(Sum('four')).values()[0]
        dee_gov_state_emis_five=dee_gov_emis_count.aggregate(Sum('five')).values()[0]
        dee_gov_state_emis_six=dee_gov_emis_count.aggregate(Sum('six')).values()[0]
        dee_gov_state_emis_seven=dee_gov_emis_count.aggregate(Sum('seven')).values()[0]
        dee_gov_state_emis_eight=dee_gov_emis_count.aggregate(Sum('eight')).values()[0]
        dee_gov_state_emis_nine=dee_gov_emis_count.aggregate(Sum('nine')).values()[0]
        dee_gov_state_emis_ten=dee_gov_emis_count.aggregate(Sum('ten')).values()[0]
        dee_gov_state_emis_eleven=dee_gov_emis_count.aggregate(Sum('eleven')).values()[0]
        dee_gov_state_emis_twelve=dee_gov_emis_count.aggregate(Sum('twelve')).values()[0]
        dee_gov_state_emis_total_count=dee_gov_emis_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'state/state_progress_report_dee.html',locals())



class District_dse_progress_report(View):
    def get(self,request,**kwargs):
        district=self.kwargs['pk']
        dee_dse=self.kwargs['pk1']
        district_name=District.objects.get(id=district)
        if dee_dse=='1' :
            school_list=School.objects.filter(district_id=district,category_id__in=[3,5,6,7,8,9,10],management_id__in=[1,2,3,4,5,6,8]).order_by('management_id')
            check=1
        else :
            school_list=School.objects.filter(district_id=district,category_id__in=[1,2,4,11,15],management_id__in=[2,3,5,6,7]).order_by('management_id')
            check=2      
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dist_dse_total_emis_one=emis_count.aggregate(Sum('one')).values()[0]
        dist_dse_total_emis_two=emis_count.aggregate(Sum('two')).values()[0]
        dist_dse_total_emis_three=emis_count.aggregate(Sum('three')).values()[0]
        dist_dse_total_emis_four=emis_count.aggregate(Sum('four')).values()[0]
        dist_dse_total_emis_five=emis_count.aggregate(Sum('five')).values()[0]
        dist_dse_total_emis_six=emis_count.aggregate(Sum('six')).values()[0]
        dist_dse_total_emis_seven=emis_count.aggregate(Sum('seven')).values()[0]
        dist_dse_total_emis_eight=emis_count.aggregate(Sum('eight')).values()[0]
        dist_dse_total_emis_nine=emis_count.aggregate(Sum('nine')).values()[0]
        dist_dse_total_emis_ten=emis_count.aggregate(Sum('ten')).values()[0]
        dist_dse_total_emis_eleven=emis_count.aggregate(Sum('eleven')).values()[0]
        dist_dse_total_emis_twelve=emis_count.aggregate(Sum('twelve')).values()[0]
        dist_dse_total_emis_total_count=emis_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'district/district_dse_progress_report.html',locals())


class District_matric_progress_report(View):
    def get(self,request,**kwargs):
        district=self.kwargs['pk']
        district_name=District.objects.get(id=district)
        school_list=School.objects.filter(district_id=district,management_id=9).order_by('management_id')
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        dist_matric_total_emis_one=emis_count.aggregate(Sum('one')).values()[0]
        dist_matric_total_emis_two=emis_count.aggregate(Sum('two')).values()[0]
        dist_matric_total_emis_three=emis_count.aggregate(Sum('three')).values()[0]
        dist_matric_total_emis_four=emis_count.aggregate(Sum('four')).values()[0]
        dist_matric_total_emis_five=emis_count.aggregate(Sum('five')).values()[0]
        dist_matric_total_emis_six=emis_count.aggregate(Sum('six')).values()[0]
        dist_matric_total_emis_seven=emis_count.aggregate(Sum('seven')).values()[0]
        dist_matric_total_emis_eight=emis_count.aggregate(Sum('eight')).values()[0]
        dist_matric_total_emis_nine=emis_count.aggregate(Sum('nine')).values()[0]
        dist_matric_total_emis_ten=emis_count.aggregate(Sum('ten')).values()[0]
        dist_matric_total_emis_eleven=emis_count.aggregate(Sum('eleven')).values()[0]
        dist_matric_total_emis_twelve=emis_count.aggregate(Sum('twelve')).values()[0]
        dist_matric_total_emis_total_count=emis_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'district/district_matric_progress_report.html',locals())



