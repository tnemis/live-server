from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from students.models import Child_detail, School_child_count
from baseapp.models import District, Block, School, Habitation, Zone
from django.core.paginator import Paginator, PageNotAnInteger

class BlockView(View):
	def get(self,request,**kwargs):
		block_id = self.request.GET.get('block_id')
		try:
			if request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4 or request.user.account.user_category_id == 3:
				if request.user.account.user_category_id == 6 or request.user.account.user_category_id == 9:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id, school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[1,2,4,12,11])
				elif request.user.account.user_category_id == 7 or request.user.account.user_category_id == 10:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id, school__management_id__in=[1,2,6,8,7,4,5], school__category_id__in=[3,5,6,7,8,9,10])
				elif request.user.account.user_category_id == 8 or request.user.account.user_category_id == 11:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id, school__management_id=9)
				elif request.user.account.user_category_id == 12 or request.user.account.user_category_id == 15:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id, school__management_id=10)
				elif request.user.account.user_category_id == 13 or request.user.account.user_category_id == 16:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id, school__management_id=11)
				elif request.user.account.user_category_id == 14 or request.user.account.user_category_id == 17:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id, school__category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
				elif request.user.account.user_category_id == 4:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id)
					Number_of_schools_in_block = School.objects.filter(block_id=block_id).count()
				elif request.user.account.user_category_id == 3:
					block_school_count = School_child_count.objects.filter(school__block_id=block_id)
				Number_of_schools_in_block = School.objects.filter(block_id=block_id).count()
				
			else:
				if request.user.account.user_category_id == 2:
					block_school_count = School_child_count.objects.filter(school__block_id=request.user.account.associated_with, school__category_id__in=[1,2,4])
					Number_of_schools_in_block = School.objects.filter(block_id=request.user.account.associated_with).count()
				elif request.user.account.user_category_id == 5:
					block_school_count = School_child_count.objects.filter(school__block_id=request.user.account.associated_with, school__category_id__in=[3,5,6,7,8,9,10])
				# return render(request,'students/block/block_detail.html',{'school_count':school_count,'page_objs':page_obj,'block_id':block_id,'Number_of_schools_in_block':Number_of_schools_in_block})
			paginator = Paginator(block_school_count, 10)
			page = request.GET.get('page')
			try:
				page_obj = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				page_obj = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				page_obj = paginator.page(paginator.num_pages)

			school_count = 0
			for sch in block_school_count:
				school_count = school_count+sch.total_count

			return render(request,'students/block/block_detail.html',{'school_count':school_count,'page_objs':page_obj,'block_id':block_id,'Number_of_schools_in_block':Number_of_schools_in_block})
		except School_child_count.DoesNotExist:
			pass
			return render(request,'students/block/block_detail.html')
		
		