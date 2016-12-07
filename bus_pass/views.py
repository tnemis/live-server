from django.views.generic import View,ListView, DetailView, CreateView, \
    DeleteView, UpdateView, \
    ArchiveIndexView, DateDetailView, \
    DayArchiveView, MonthArchiveView, \
    TodayArchiveView, WeekArchiveView, \
    YearArchiveView
from django.contrib import messages
from django.shortcuts import render
from students.models import Child_detail, Child_family_detail, School_child_count, Parent_annual_income
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


class Name_list(View):
	def get(self,request,**kwargs):
		school=self.kwargs['school']
		cls=self.kwargs['cls']
		a=Child_detail.objects.filter(bus_pass="Yes",school_id=school,class_studying_id=cls)
		return render(request,'bus_pass/school/name_list.html',locals())

class Name_list_all(View):
	def get(self,request,**kwargs):
		school1=self.kwargs['school']
		school=School.objects.filter(id=school1)
		a=Child_detail.objects.filter(bus_pass="Yes",school_id=school).order_by('class_studying')
		for i in a:
			print i.name
			
		return render(request,'bus_pass/school/name_list_all.html',locals())




class SchoolBusPassReport(View):
	def get(self,request,**kwargs):
		school=self.kwargs['pk']
		lisst=School.objects.filter(id=school)
		a=Child_detail.objects.filter(bus_pass="Yes",school_id=school).values('class_studying','school').annotate(x=Count('school')).order_by('school')
		st=Child_detail.objects.filter(bus_pass="Yes",school_id=school,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).values('school').annotate(y=Count('class_studying'))
		bt=Child_detail.objects.filter(bus_pass="Yes",school_id=school).values('class_studying').annotate(z=Count('class_studying'))
		total=Child_detail.objects.filter(bus_pass="Yes",school_id=school,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).count()
		

		return render(request,'bus_pass/school/school_bus_pass_report.html',locals())

	


class BlockBusPassReport(View):
	def get(self,request,**kwargs):
		blk=self.kwargs['pk']
		blck=Block.objects.get(id=blk)
		lisst=School.objects.filter(block_id=blk).order_by('id')
		a=Child_detail.objects.filter(bus_pass="Yes",block_id=blk).values('class_studying','school').annotate(x=Count('school')).order_by('school')
		st=Child_detail.objects.filter(bus_pass="Yes",block_id=blk,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).values('school').annotate(y=Count('class_studying'))
		bt=Child_detail.objects.filter(bus_pass="Yes",block_id=blk).values('class_studying').annotate(z=Count('class_studying'))
		total=Child_detail.objects.filter(bus_pass="Yes",block_id=blk,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).count()
		return render(request,'bus_pass/moniter/block_bus_pass_report.html',locals())

	


class DistrictBusPassReport(View):
	def get(self,request,**kwargs):
		dist=self.kwargs['pk']
		dist_name=District.objects.get(id=dist)
		lisst=Block.objects.filter(district_id=dist, block_type="block").order_by('id')
		a=Child_detail.objects.filter(district_id=dist,bus_pass="Yes").values('class_studying','block').annotate(x=Count('block')).order_by('block')
		st=Child_detail.objects.filter(bus_pass="Yes",district_id=dist,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).values('block').annotate(y=Count('class_studying'))
		bt=Child_detail.objects.filter(bus_pass="Yes",district_id=dist).values('class_studying').annotate(z=Count('class_studying'))
		total=Child_detail.objects.filter(bus_pass="Yes",district_id=dist,class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).count()
		return render(request,'bus_pass/moniter/district_bus_pass_report.html',locals())

	

class StateBusPassReport(View):
	def get(self,request,**kwargs):
		lisst=District.objects.all().exclude(district_name='None').order_by('id')
		a=Child_detail.objects.filter(bus_pass="Yes").values('class_studying','district').annotate(x=Count('district')).order_by('district')		
		st=Child_detail.objects.filter(bus_pass="Yes",class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).values('district').annotate(y=Count('class_studying'))
		bt=Child_detail.objects.filter(bus_pass="Yes").values('class_studying').annotate(z=Count('class_studying'))
		total=Child_detail.objects.filter(bus_pass="Yes",class_studying_id__in=[1,2,3,4,5,6,7,8,9,10,11,12]).count()
		# paginator = Paginator(lisst,17) 
		# page = request.GET.get('page')
		# try:
		# 	lisst = paginator.page(page)
		# except PageNotAnInteger:
		# 	lisst = paginator.page(1)
		# except EmptyPage:
		# 	lisst = paginator.page(paginator.num_pages)
		
		return render(request,'bus_pass/moniter/state_bus_pass_report.html',locals())

		
	

