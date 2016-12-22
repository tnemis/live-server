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
from udise.models import *
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



class State_level_udise_report(View):
    def get(self,request,**kwargs):
    	district=District.objects.all()
    	c1_total=Udise_count.objects.aggregate(Sum('c1')).values()[0]
        return render(request,'state/state_udise_report.html',locals())



class School_level_udise_report(View):
    def get(self,request,**kwargs):
        school=self.kwargs['pk']
        school_id=School.objects.get(school_code=school)
        try:
            udise_count=Udise_count.objects.get(school_code=school)
            udise_id=udise_count.school_id
            emis_students=School_child_count.objects.get(school_id=udise_id)
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
            diff_1=(udise_count.c1)-(emis_count_one)
            diff_2=(udise_count.c2)-(emis_count_two)
            diff_3=(udise_count.c3)-(emis_count_three)
            diff_4=(udise_count.c4)-(emis_count_four)
            diff_5=(udise_count.c5)-(emis_count_five)
            diff_6=(udise_count.c6)-(emis_count_six)
            diff_7=(udise_count.c7)-(emis_count_seven)
            diff_8=(udise_count.c8)-(emis_count_eight)
            diff_9=(udise_count.c9)-(emis_count_nine)
            diff_10=(udise_count.c10)-(emis_count_ten)
            diff_11=(udise_count.c11)-(emis_count_eleven)
            diff_12=(udise_count.c12)-(emis_count_twelve)
            diff_total=(udise_count.school_total)-(emis_count_total_count)
            return render(request,'school/school_udise_report.html',locals())
        except:
            no_udise='you didnot submit udise report'
            return render(request,'school/school_udise_report.html',locals())


class Block_level_udise_report(View):
    def get(self,request,**kwargs):
        block=self.kwargs['pk']
        block_name=Block.objects.get(id=block)
        udise_count=Udise_count.objects.filter(block_id=block)
        school_list=School.objects.filter(block_id=block)
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        udise_block_total=0
        for i in udise_count:
            udise_block_total=udise_block_total+i.school_total
        emis_block_total=0
        for j in emis_count:
        	emis_block_total=emis_block_total+j.total_count
        diff_block_total=udise_block_total-emis_block_total
        block_udise_c1=udise_count.aggregate(Sum('c1')).values()[0]
        block_udise_c2=udise_count.aggregate(Sum('c2')).values()[0]
        block_udise_c3=udise_count.aggregate(Sum('c3')).values()[0]
        block_udise_c4=udise_count.aggregate(Sum('c4')).values()[0]
        block_udise_c5=udise_count.aggregate(Sum('c5')).values()[0]
        block_udise_c6=udise_count.aggregate(Sum('c6')).values()[0]
        block_udise_c7=udise_count.aggregate(Sum('c7')).values()[0]
        block_udise_c8=udise_count.aggregate(Sum('c8')).values()[0]
        block_udise_c9=udise_count.aggregate(Sum('c9')).values()[0]
        block_udise_c10=udise_count.aggregate(Sum('c10')).values()[0]
        block_udise_c11=udise_count.aggregate(Sum('c11')).values()[0]
        block_udise_c12=udise_count.aggregate(Sum('c12')).values()[0]
        block_udise_school_total=udise_count.aggregate(Sum('school_total')).values()[0]
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
        block_diff_1=(block_udise_c1)-(block_emis_one)
        block_diff_2=(block_udise_c2)-(block_emis_two)
        block_diff_3=(block_udise_c3)-(block_emis_three)
        block_diff_4=(block_udise_c4)-(block_emis_four)
        block_diff_5=(block_udise_c5)-(block_emis_five)
        block_diff_6=(block_udise_c6)-(block_emis_six)
        block_diff_7=(block_udise_c7)-(block_emis_seven)
        block_diff_8=(block_udise_c8)-(block_emis_eight)
        block_diff_9=(block_udise_c9)-(block_emis_nine)
        block_diff_10=(block_udise_c10)-(block_emis_ten)
        block_diff_11=(block_udise_c11)-(block_emis_eleven)
        block_diff_12=(block_udise_c12)-(block_emis_twelve)
        block_diff_total=(block_udise_school_total)-(block_emis_total_count)
        return render(request,'block/block_udise_report.html',locals())
   
      
class District_level_udise_report(View):
    def get(self,request,**kwargs):
        user=self.kwargs['pk']
        district=District.objects.get(id=user)
        blocks=Block.objects.filter(district_id=user)
        block_ids=[]
        block_names=[]
        block_udise_school_total_list=[]
        block_emis_school_total_list=[]
        for i in blocks:
            udise_count=Udise_count.objects.filter(block_id=i.id)
            block_udise_school_total=udise_count.aggregate(Sum('school_total'))
            block_udise_school_total_list+=block_udise_school_total.values()
            block_ids.append(str(i.id))
            block_names.append(i.block_name)
            school_ids=udise_count.values_list('school_id', flat=True)
            school_list=School.objects.filter(id__in=school_ids)
            emis_count=School_child_count.objects.filter(school_id__in=school_list)
            block_emis_total=emis_count.aggregate(Sum('total_count'))
            block_emis_school_total_list+=block_emis_total.values()
        mylist=zip(block_ids,block_names,block_udise_school_total_list,block_emis_school_total_list)
        udise_district_total=0
        emis_district_total=0
        for a,b,c,d in mylist:
            udise_district_total+=c
            emis_district_total+=d
        diff_district_total=udise_district_total - emis_district_total
        udise_count=Udise_count.objects.filter(district_id=user)
        print len(udise_count)
        school_ids=udise_count.values_list('school_id', flat=True)
        school_list=School.objects.filter(id__in=school_ids)
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        district_udise_c1=udise_count.aggregate(Sum('c1')).values()[0]
        district_udise_c2=udise_count.aggregate(Sum('c2')).values()[0]
        district_udise_c3=udise_count.aggregate(Sum('c3')).values()[0]
        district_udise_c4=udise_count.aggregate(Sum('c4')).values()[0]
        district_udise_c5=udise_count.aggregate(Sum('c5')).values()[0]
        district_udise_c6=udise_count.aggregate(Sum('c6')).values()[0]
        district_udise_c7=udise_count.aggregate(Sum('c7')).values()[0]
        district_udise_c8=udise_count.aggregate(Sum('c8')).values()[0]
        district_udise_c9=udise_count.aggregate(Sum('c9')).values()[0]
        district_udise_c10=udise_count.aggregate(Sum('c10')).values()[0]
        district_udise_c11=udise_count.aggregate(Sum('c11')).values()[0]
        district_udise_c12=udise_count.aggregate(Sum('c12')).values()[0]
        district_udise_school_total=udise_count.aggregate(Sum('school_total')).values()[0]
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
        district_diff_1=(district_udise_c1)-(district_emis_one)
        district_diff_2=(district_udise_c2)-(district_emis_two)
        district_diff_3=(district_udise_c3)-(district_emis_three)
        district_diff_4=(district_udise_c4)-(district_emis_four)
        district_diff_5=(district_udise_c5)-(district_emis_five)
        district_diff_6=(district_udise_c6)-(district_emis_six)
        district_diff_7=(district_udise_c7)-(district_emis_seven)
        district_diff_8=(district_udise_c8)-(district_emis_eight)
        district_diff_9=(district_udise_c9)-(district_emis_nine)
        district_diff_10=(district_udise_c10)-(district_emis_ten)
        district_diff_11=(district_udise_c11)-(district_emis_eleven)
        district_diff_12=(district_udise_c12)-(district_emis_twelve)
        district_diff_total=(district_udise_school_total)-(district_emis_total_count)
        return render(request,'district/district_udise_report.html',locals())


class State_level_udise_report(View):
    def get(self,request,**kwargs):
        district=District.objects.all()
        district_ids=[]
        district_names=[]
        district_udise_school_total_list=[]
        district_emis_school_total_list=[]
        for i in district:
            udise_count=Udise_count.objects.filter(district_id=i.id)
            district_udise_school_total=udise_count.aggregate(Sum('school_total'))
            district_udise_school_total_list+=  0 if udise_count == None  else district_udise_school_total.values()
            district_ids.append(str(i.id))
            district_names.append(i.district_name)
            school_ids=udise_count.values_list('school_id', flat=True)
            school_list=School.objects.filter(id__in=school_ids)
            emis_count=School_child_count.objects.filter(school_id__in=school_list)
            district_emis_total=emis_count.aggregate(Sum('total_count'))
            district_emis_school_total_list+=district_emis_total.values()
        mylist=zip(district_ids,district_names,district_udise_school_total_list,district_emis_school_total_list)
        print mylist
        udise_state_total=0
        emis_state_total=0
        for x,p,y,z in mylist:
            udise_state_total+=y
            emis_state_total+=z
        diff_state_total=udise_state_total - emis_state_total
        udise_count=Udise_count.objects.all()
        print len(udise_count)
        school_ids=udise_count.values_list('school_id', flat=True)
        school_list=School.objects.filter(id__in=school_ids)
        emis_count=School_child_count.objects.filter(school_id__in=school_list)
        state_udise_c1=udise_count.aggregate(Sum('c1')).values()[0]
        state_udise_c2=udise_count.aggregate(Sum('c2')).values()[0]
        state_udise_c3=udise_count.aggregate(Sum('c3')).values()[0]
        state_udise_c4=udise_count.aggregate(Sum('c4')).values()[0]
        state_udise_c5=udise_count.aggregate(Sum('c5')).values()[0]
        state_udise_c6=udise_count.aggregate(Sum('c6')).values()[0]
        state_udise_c7=udise_count.aggregate(Sum('c7')).values()[0]
        state_udise_c8=udise_count.aggregate(Sum('c8')).values()[0]
        state_udise_c9=udise_count.aggregate(Sum('c9')).values()[0]
        state_udise_c10=udise_count.aggregate(Sum('c10')).values()[0]
        state_udise_c11=udise_count.aggregate(Sum('c11')).values()[0]
        state_udise_c12=udise_count.aggregate(Sum('c12')).values()[0]
        state_udise_school_total=udise_count.aggregate(Sum('school_total')).values()[0]
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
        state_diff_1=(state_udise_c1)-(state_emis_one)
        state_diff_2=(state_udise_c2)-(state_emis_two)
        state_diff_3=(state_udise_c3)-(state_emis_three)
        state_diff_4=(state_udise_c4)-(state_emis_four)
        state_diff_5=(state_udise_c5)-(state_emis_five)
        state_diff_6=(state_udise_c6)-(state_emis_six)
        state_diff_7=(state_udise_c7)-(state_emis_seven)
        state_diff_8=(state_udise_c8)-(state_emis_eight)
        state_diff_9=(state_udise_c9)-(state_emis_nine)
        state_diff_10=(state_udise_c10)-(state_emis_ten)
        state_diff_11=(state_udise_c11)-(state_emis_eleven)
        state_diff_12=(state_udise_c12)-(state_emis_twelve)
        state_diff_total=(state_udise_school_total)-(state_emis_total_count)
        return render(request,'state/state_udise_report.html',locals())


        
