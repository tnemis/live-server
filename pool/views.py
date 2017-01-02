from django.views.generic import View,ListView, DetailView, CreateView, \
    DeleteView, UpdateView, \
    ArchiveIndexView, DateDetailView, \
    DayArchiveView, MonthArchiveView, \
    TodayArchiveView, WeekArchiveView, \
    YearArchiveView
from django.contrib import messages
from django.shortcuts import render
from students.models import *
from django.db.models import Q
from baseapp.models import*
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger
from datetime import datetime
from django import template
from django.contrib import messages
from excel_response import ExcelResponse
from django.db.models import *
from django.contrib.auth.decorators import *




class SchoolPoolReport(View):
	def get(self,request,**kwargs):
		school=self.kwargs['pk']
		school=School.objects.get(id=school)
		my_students=st=Child_detail.objects.filter(transfer_flag__in=[1],school_id=school,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12])
		return render(request,'pool/school/name_list.html',locals())
	


class BlockPoolReport(View):
	def get(self,request,**kwargs):
		blk=self.kwargs['pk']
		blck=Block.objects.get(id=blk)
		school_list=School.objects.filter(block_id=blk).order_by('id')
		pool_count=Pool_child_count.objects.filter(school_id__in=school_list)
		block_emis_one=pool_count.aggregate(Sum('one')).values()[0]
		block_emis_two=pool_count.aggregate(Sum('two')).values()[0]
		block_emis_three=pool_count.aggregate(Sum('three')).values()[0]
		block_emis_four=pool_count.aggregate(Sum('four')).values()[0]
		block_emis_five=pool_count.aggregate(Sum('five')).values()[0]
		block_emis_six=pool_count.aggregate(Sum('six')).values()[0]
		block_emis_seven=pool_count.aggregate(Sum('seven')).values()[0]
		block_emis_eight=pool_count.aggregate(Sum('eight')).values()[0]
		block_emis_nine=pool_count.aggregate(Sum('nine')).values()[0]
		block_emis_ten=pool_count.aggregate(Sum('ten')).values()[0]
		block_emis_eleven=pool_count.aggregate(Sum('eleven')).values()[0]
		block_emis_twelve=pool_count.aggregate(Sum('twelve')).values()[0]
		block_emis_total_count=pool_count.aggregate(Sum('total_count')).values()[0]
		return render(request,'pool/moniter/block_pool_report.html',locals())
	
   
class DistrictPoolReport(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3]
        user=self.kwargs['pk']
        district=District.objects.get(id=user)
        blocks=Block.objects.filter(district_id=user)
        block_ids=[]
        block_names=[]
        block_pool_one=[]
        block_pool_two=[]
        block_pool_three=[]
        block_pool_four=[]
        block_pool_five=[]
        block_pool_six=[]
        block_pool_seven=[]
        block_pool_eight=[]
        block_pool_nine=[]
        block_pool_ten=[]
        block_pool_eleven=[]
        block_pool_twelve=[]
        block_pool_total_count=[]
        for i in blocks:
            block_ids.append(str(i.id))
            block_names.append(i.block_name)
            school_list=School.objects.filter(block_id=i.id)
            pool_count=Pool_child_count.objects.filter(school_id__in=school_list)
            block_pool_total_one=pool_count.aggregate(Sum('one'))
            block_pool_total_two=pool_count.aggregate(Sum('two'))
            block_pool_total_three=pool_count.aggregate(Sum('three'))
            block_pool_total_four=pool_count.aggregate(Sum('four'))
            block_pool_total_five=pool_count.aggregate(Sum('five'))
            block_pool_total_six=pool_count.aggregate(Sum('six'))
            block_pool_total_seven=pool_count.aggregate(Sum('seven'))
            block_pool_total_eight=pool_count.aggregate(Sum('eight'))
            block_pool_total_nine=pool_count.aggregate(Sum('nine'))
            block_pool_total_ten=pool_count.aggregate(Sum('ten'))
            block_pool_total_eleven=pool_count.aggregate(Sum('eleven'))
            block_pool_total_twelve=pool_count.aggregate(Sum('twelve'))
            block_pool_total_total_count=pool_count.aggregate(Sum('total_count'))
            block_pool_one+=block_pool_total_one.values()
            block_pool_two+=block_pool_total_two.values()
            block_pool_three+=block_pool_total_three.values()
            block_pool_four+=block_pool_total_four.values()
            block_pool_five+=block_pool_total_five.values()
            block_pool_six+=block_pool_total_six.values()
            block_pool_seven+=block_pool_total_seven.values()
            block_pool_eight+=block_pool_total_eight.values()
            block_pool_nine+=block_pool_total_nine.values()
            block_pool_ten+=block_pool_total_ten.values()
            block_pool_eleven+=block_pool_total_eleven.values()
            block_pool_twelve+=block_pool_total_twelve.values()
            block_pool_total_count+=block_pool_total_total_count.values()
        mylist=zip(block_ids,block_names,block_pool_one,block_pool_two,block_pool_three,block_pool_four,block_pool_five,block_pool_six,block_pool_seven,block_pool_eight,block_pool_nine,block_pool_ten,block_pool_eleven,block_pool_twelve,block_pool_total_count)
        school_list=School.objects.filter(district_id=district)
        pool_count=Pool_child_count.objects.filter(school_id__in=school_list)
        district_pool_one=pool_count.aggregate(Sum('one')).values()[0]
        district_pool_two=pool_count.aggregate(Sum('two')).values()[0]
        district_pool_three=pool_count.aggregate(Sum('three')).values()[0]
        district_pool_four=pool_count.aggregate(Sum('four')).values()[0]
        district_pool_five=pool_count.aggregate(Sum('five')).values()[0]
        district_pool_six=pool_count.aggregate(Sum('six')).values()[0]
        district_pool_seven=pool_count.aggregate(Sum('seven')).values()[0]
        district_pool_eight=pool_count.aggregate(Sum('eight')).values()[0]
        district_pool_nine=pool_count.aggregate(Sum('nine')).values()[0]
        district_pool_ten=pool_count.aggregate(Sum('ten')).values()[0]
        district_pool_eleven=pool_count.aggregate(Sum('eleven')).values()[0]
        district_pool_twelve=pool_count.aggregate(Sum('twelve')).values()[0]
        district_pool_total_count=pool_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'pool/moniter/district_pool_report.html',locals())



class StatePoolReport(View):
    def get(self,request,**kwargs):
        districts=District.objects.all()
        district_ids=[]
        district_names=[]
        district_pool_one=[]
        district_pool_two=[]
        district_pool_three=[]
        district_pool_four=[]
        district_pool_five=[]
        district_pool_six=[]
        district_pool_seven=[]
        district_pool_eight=[]
        district_pool_nine=[]
        district_pool_ten=[]
        district_pool_eleven=[]
        district_pool_twelve=[]
        district_pool_total_count=[]
        for i in districts:
            district_ids.append(str(i.id))
            district_names.append(i.district_name)
            school_list=School.objects.filter(district_id=i.id)
            pool_count=Pool_child_count.objects.filter(school_id__in=school_list)
            district_pool_total_one=pool_count.aggregate(Sum('one'))
            district_pool_total_two=pool_count.aggregate(Sum('two'))
            district_pool_total_three=pool_count.aggregate(Sum('three'))
            district_pool_total_four=pool_count.aggregate(Sum('four'))
            district_pool_total_five=pool_count.aggregate(Sum('five'))
            district_pool_total_six=pool_count.aggregate(Sum('six'))
            district_pool_total_seven=pool_count.aggregate(Sum('seven'))
            district_pool_total_eight=pool_count.aggregate(Sum('eight'))
            district_pool_total_nine=pool_count.aggregate(Sum('nine'))
            district_pool_total_ten=pool_count.aggregate(Sum('ten'))
            district_pool_total_eleven=pool_count.aggregate(Sum('eleven'))
            district_pool_total_twelve=pool_count.aggregate(Sum('twelve'))
            district_pool_total_total_count=pool_count.aggregate(Sum('total_count'))
            district_pool_one+=district_pool_total_one.values()
            district_pool_two+=district_pool_total_two.values()
            district_pool_three+=district_pool_total_three.values()
            district_pool_four+=district_pool_total_four.values()
            district_pool_five+=district_pool_total_five.values()
            district_pool_six+=district_pool_total_six.values()
            district_pool_seven+=district_pool_total_seven.values()
            district_pool_eight+=district_pool_total_eight.values()
            district_pool_nine+=district_pool_total_nine.values()
            district_pool_ten+=district_pool_total_ten.values()
            district_pool_eleven+=district_pool_total_eleven.values()
            district_pool_twelve+=district_pool_total_twelve.values()
            district_pool_total_count+=district_pool_total_total_count.values()
        mylist=zip(district_ids,district_names,district_pool_one,district_pool_two,district_pool_three,district_pool_four,district_pool_five,district_pool_six,district_pool_seven,district_pool_eight,district_pool_nine,district_pool_ten,district_pool_eleven,district_pool_twelve,district_pool_total_count)
        pool_count=Pool_child_count.objects.all()
        state_pool_one=pool_count.aggregate(Sum('one')).values()[0]
        state_pool_two=pool_count.aggregate(Sum('two')).values()[0]
        state_pool_three=pool_count.aggregate(Sum('three')).values()[0]
        state_pool_four=pool_count.aggregate(Sum('four')).values()[0]
        state_pool_five=pool_count.aggregate(Sum('five')).values()[0]
        state_pool_six=pool_count.aggregate(Sum('six')).values()[0]
        state_pool_seven=pool_count.aggregate(Sum('seven')).values()[0]
        state_pool_eight=pool_count.aggregate(Sum('eight')).values()[0]
        state_pool_nine=pool_count.aggregate(Sum('nine')).values()[0]
        state_pool_ten=pool_count.aggregate(Sum('ten')).values()[0]
        state_pool_eleven=pool_count.aggregate(Sum('eleven')).values()[0]
        state_pool_twelve=pool_count.aggregate(Sum('twelve')).values()[0]
        state_pool_total_count=pool_count.aggregate(Sum('total_count')).values()[0]
        return render(request,'pool/moniter/state_pool_report.html',locals())


		
	

