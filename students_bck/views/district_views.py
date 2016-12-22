from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from students.models import Child_detail, School_child_count
from baseapp.models import District, Block, School, Habitation, Zone
from django.core.paginator import Paginator, PageNotAnInteger
from collections import namedtuple

class DistrictView(View):
	def get(self,request,**kwargs):
		district_id = self.request.GET.get('district_id')
		try:
			if request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
				block_list= Block.objects.filter(district_id=district_id).order_by('block_name')
				if request.user.account.user_category_id == 9:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id, school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[1,2,4,12,11])
				elif request.user.account.user_category_id == 10:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id, school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[3,5,6,7,8,9,10])
				elif request.user.account.user_category_id == 11:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id, school__management_id=9)
				elif request.user.account.user_category_id == 15:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id, school__management_id=10)
				elif request.user.account.user_category_id == 16:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id, school__management_id=11)
				elif request.user.account.user_category_id == 17:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id, school__category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
				elif request.user.account.user_category_id == 4:
					district_school_count = School_child_count.objects.filter(school__district_id=district_id) 
				Number_of_blocks_in_district = Block.objects.filter(district_id=district_id).count()
				Number_of_schools_in_district = School.objects.filter(district_id=district_id).count()

			else:
				block_list= Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
				if request.user.account.user_category_id == 6:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[1,2,4,12,11])
				elif request.user.account.user_category_id == 7:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[3,5,6,7,8,9,10])
				elif request.user.account.user_category_id == 8:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__management_id=9)
				elif request.user.account.user_category_id == 12:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__management_id=10)
				elif request.user.account.user_category_id == 13:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__management_id=11)
				elif request.user.account.user_category_id == 14:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
				elif request.user.account.user_category_id == 3:
					district_school_count = School_child_count.objects.filter(school__district_id=request.user.account.associated_with, school__management_id__in=[1,2,6,8,7,4,5,9], school__category_id__in=[1,2,3,4,5,6,7,8,9,10,11,12])
				Number_of_blocks_in_district = Block.objects.filter(district_id=request.user.account.associated_with).count()
				Number_of_schools_in_district = School.objects.filter(district_id=request.user.account.associated_with).count()
				# return render(request,'students/district/district_detail.html',{'student_count':student_count,'page_objs':page_obj,'district_id':district_id,'Number_of_blocks_in_district':Number_of_blocks_in_district,'Number_of_schools_in_district':Number_of_schools_in_district})	
			student_count = 0
			for sch in district_school_count:
				student_count = student_count+sch.total_count
			
			for blk in block_list:
				block_list_count=[]
				blk_student_count=0
				blk_count = district_school_count.filter(school__block_id=blk.id)
				for stu in blk_count:
					blk_student_count = blk_student_count+stu.total_count
				block_list_count = [blk.block_name,blk_student_count,blk.id]
				MyStruct = namedtuple('MyStruct', 'a')
				try:
					s= s+MyStruct(a=block_list_count)
				except Exception:
					s= MyStruct(a=block_list_count)
			
			paginator = Paginator(s, 10)
			page = request.GET.get('page')
			try:
				page_obj = paginator.page(page)
			except PageNotAnInteger:
				page_obj = paginator.page(1)
			except EmptyPage:
				page_obj = paginator.page(paginator.num_pages)
			return render(request,'students/district/district_detail.html',{'student_count':student_count,'page_objs':page_obj,'district_id':district_id,'Number_of_blocks_in_district':Number_of_blocks_in_district,'Number_of_schools_in_district':Number_of_schools_in_district})	
		except School_child_count.DoesNotExist:
			pass
			return render(request,'students/district/district_detail.html')
		
		