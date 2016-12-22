from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from students.models import Child_detail, School_child_count
from baseapp.models import District, Block, School, Habitation, Zone
from django.core.paginator import Paginator, PageNotAnInteger
from collections import namedtuple


class StateView(View):
	def get(self,request,**kwargs):
		try:
			district_list= District.objects.all().order_by('district_name')
			if request.user.account.user_category_id == 9:
				state_school_count = School_child_count.objects.filter(school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[1,2,4,12,11])
			elif request.user.account.user_category_id == 10:
				state_school_count = School_child_count.objects.filter(school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[3,5,6,7,8,9,10])
			elif request.user.account.user_category_id == 11:
				state_school_count = School_child_count.objects.filter(school__management_id=9)
			elif request.user.account.user_category_id == 15:
				state_school_count = School_child_count.objects.filter(school__management_id=10)
			elif request.user.account.user_category_id == 16:
				state_school_count = School_child_count.objects.filter(school__management_id=11)
			elif request.user.account.user_category_id == 17:
				state_school_count = School_child_count.objects.filter(school__category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
			elif request.user.account.user_category_id == 4:
				state_school_count = School_child_count.objects.all() 
				student_count = Child_detail.objects.all().count()
				Number_of_districts_in_state = District.objects.all().count()
				Number_of_blocks_in_state = Block.objects.all().count()
				Number_of_schools_in_state = School.objects.all().count()

			# student_count = 0
			# for sch in state_school_count:
			# 	student_count = student_count+sch.total_count
			
			for dist in district_list:
				dist_list_count=[]
				dist_student_count=0
				dist_count = state_school_count.filter(school__district_id=dist.id)
				for stu in dist_count:
					dist_student_count = dist_student_count+stu.total_count
				dist_list_count = [dist.district_name,dist_student_count,dist.id]
				MyList = namedtuple('MyList','a')
				try:
					s=s+MyList(a=dist_list_count)
				except Exception:
					s=MyList(a=dist_list_count)

			paginator = Paginator(s, 10)
			page = request.GET.get('page')
			try:
				page_obj = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				page_obj = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				page_obj = paginator.page(paginator.num_pages)

			return render(request,'students/state/state_detail.html',{'student_count':student_count,'page_objs':page_obj,'Number_of_districts_in_state':Number_of_districts_in_state,'Number_of_blocks_in_state':Number_of_blocks_in_state,'Number_of_schools_in_state':Number_of_schools_in_state})
		except School_child_count.DoesNotExist:
			pass
			return render(request,'students/state/state_detail.html')
		
	# def post(self,request,**kwargs):
	# 	if request.POST['state_id'] == '1':
	# 		school_list = School.objects.filter(category_id__in=[1,2,4])
	# 	elif request.POST['state_id'] == '2':
	# 		school_list = School.objects.filter(category_id__in=[3,5,6,7,8,9,10])
	# 	elif request.POST['state_id'] == '3':
	# 		school_list = School.objects.filter(management_id=9)
        
 #        paginator = Paginator(school_list, 10)
 #        page = request.GET.get('page')
 #        try:
 #            page_obj = paginator.page(page)
 #        except PageNotAnInteger:
 #            page_obj = paginator.page(1)
 #        except EmptyPage:
 #            page_obj = paginator.page(paginator.num_pages)
 #        return render(request,'students/state/state_detail.html',{'school_list':school_list,'page_objs':page_obj})

	# 	