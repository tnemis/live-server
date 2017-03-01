from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from students.models import Child_detail, School_child_count
from baseapp.models import *
from progress.models import *
from django.db.models import Count, Sum
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache



# Create your views here.

class state_level_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			dse_school_list=School.objects.filter(management_id__in= [1,2,4,5],category_id__in=[3,5,6,7,8,9,10])
			dse=aadhaar_student_count.objects.filter(school_id__in=dse_school_list)
			dse_emis=0
			dse_aadhaar=0
			dse_not_aadhaar=0
			for i in dse:
				dse_emis=dse_emis+i.school_total
				dse_aadhaar=dse_aadhaar+i.a_school_total
			dse_not_aadhaar=dse_emis-dse_aadhaar

			p_a_school_list=School.objects.filter(management_id__in=[6,7],category_id__in=[3,5,6,7,8,9,10])
			pvt_aided=aadhaar_student_count.objects.filter(school_id__in=p_a_school_list)
			pvt_aided_emis=0
			pvt_aided_aadhaar=0
			pvt_aided_not_aadhaar=0
			for i in pvt_aided:
				pvt_aided_emis=pvt_aided_emis+i.school_total
				pvt_aided_aadhaar=pvt_aided_aadhaar+i.a_school_total
			pvt_aided_not_aadhaar=pvt_aided_emis-pvt_aided_aadhaar

			p_u_school_list=School.objects.filter(management_id__in=[8,12,13,14,15,16,17],category_id__in=[3,5,6,7,8,9,10])
			pvt_unaided=aadhaar_student_count.objects.filter(school_id__in=p_u_school_list)
			pvt_unaided_emis=0
			pvt_unaided_aadhaar=0
			pvt_unaided_not_aadhaar=0
			for i in pvt_unaided:
				pvt_unaided_emis=pvt_unaided_emis+i.school_total
				pvt_unaided_aadhaar=pvt_unaided_aadhaar+i.a_school_total
			pvt_unaided_not_aadhaar=pvt_unaided_emis-pvt_unaided_aadhaar

			matriculation_school_list=School.objects.filter(management_id__in=[9])
			matric=aadhaar_student_count.objects.filter(school_id__in=matriculation_school_list)
			matric_emis=0
			matric_aadhaar=0
			matric_not_aadhaar=0
			for i in matric:
				matric_emis=matric_emis+i.school_total
				matric_aadhaar=matric_aadhaar+i.a_school_total
			matric_not_aadhaar=matric_emis-matric_aadhaar

			cbse_school_list=School.objects.filter(management_id__in=[10,11])
			cbse=aadhaar_student_count.objects.filter(school_id__in=cbse_school_list)
			cbse_emis=0
			cbse_aadhaar=0
			cbse_not_aadhaar=0
			for i in cbse:
				cbse_emis=cbse_emis+i.school_total
				cbse_aadhaar=cbse_aadhaar+i.a_school_total
			cbse_not_aadhaar=cbse_emis-cbse_aadhaar

# dee
			
			dee_school_list=School.objects.filter(management_id__in=[1,2,3,4,5],category_id__in=[1,2,4,11,15])
			dee=aadhaar_student_count.objects.filter(school_id__in=dee_school_list)
			dee_emis=0
			dee_aadhaar=0
			dee_not_aadhaar=0
			for i in dee:
				dee_emis=dee_emis+i.school_total
				dee_aadhaar=dee_aadhaar+i.a_school_total
			dee_not_aadhaar=dee_emis-dee_aadhaar

			d_p_a_school_list=School.objects.filter(management_id__in=[6,7],category_id__in=[1,2,4,11,15])
			dee_p_a=aadhaar_student_count.objects.filter(school_id__in=d_p_a_school_list)
			dee_p_a_emis=0
			dee_p_a_aadhaar=0
			dee_p_a_not_aadhaar=0
			for i in dee_p_a:
				dee_p_a_emis=dee_p_a_emis+i.school_total
				dee_p_a_aadhaar=dee_p_a_aadhaar+i.a_school_total
			dee_p_a_not_aadhaar=dee_p_a_emis-dee_p_a_aadhaar

			nursery_school_list=School.objects.filter(management_id__in=[8,12,13,14,15,16,17],category_id__in=[1,2,4,11,15])
			dee_n=aadhaar_student_count.objects.filter(school_id__in=nursery_school_list)
			dee_n_emis=0
			dee_n_aadhaar=0
			dee_n_not_aadhaar=0
			for i in dee_n:
				dee_n_emis=dee_n_emis+i.school_total
				dee_n_aadhaar=dee_n_aadhaar+i.a_school_total
			dee_n_not_aadhaar=dee_n_emis-dee_n_aadhaar


			return render(request,'aadhaar/state/aadhaar_report.html',locals())

class state_level_aadhaar_report_dee(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			
# dee
			dee_school_list=School.objects.filter(management_id__in=[1,2,3,4,5],category_id__in=[1,2,4,11,15])
			dee=aadhaar_student_count.objects.filter(school_id__in=dee_school_list)
			dee_emis=0
			dee_aadhaar=0
			dee_not_aadhaar=0
			for i in dee:
				dee_emis=dee_emis+i.school_total
				dee_aadhaar=dee_aadhaar+i.a_school_total
			dee_not_aadhaar=dee_emis-dee_aadhaar

			d_p_a_school_list=School.objects.filter(management_id__in=[6,7],category_id__in=[1,2,4,11,15])
			dee_p_a=aadhaar_student_count.objects.filter(school_id__in=d_p_a_school_list)
			dee_p_a_emis=0
			dee_p_a_aadhaar=0
			dee_p_a_not_aadhaar=0
			for i in dee_p_a:
				dee_p_a_emis=dee_p_a_emis+i.school_total
				dee_p_a_aadhaar=dee_p_a_aadhaar+i.a_school_total
			dee_p_a_not_aadhaar=dee_p_a_emis-dee_p_a_aadhaar

			nursery_school_list=School.objects.filter(management_id__in=[8,12,13,14,15,16,17],category_id__in=[1,2,4,11,15])
			dee_n=aadhaar_student_count.objects.filter(school_id__in=nursery_school_list)
			dee_n_emis=0
			dee_n_aadhaar=0
			dee_n_not_aadhaar=0
			for i in dee_n:
				dee_n_emis=dee_n_emis+i.school_total
				dee_n_aadhaar=dee_n_aadhaar+i.a_school_total
			dee_n_not_aadhaar=dee_n_emis-dee_n_aadhaar


			return render(request,'aadhaar/state/s_l_aadhaar_dee_report.html',locals())



class matric_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			matriculation_school_list=School.objects.filter(management_id__in=[9])
			matric=aadhaar_student_count.objects.filter(school_id__in=matriculation_school_list)
			matric_emis=0
			matric_aadhaar=0
			matric_not_aadhaar=0
			for i in matric:
				matric_emis=matric_emis+i.school_total
				matric_aadhaar=matric_aadhaar+i.a_school_total
			matric_not_aadhaar=matric_emis-matric_aadhaar



			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			m_emis=[]
			m_aadhaar=[]
			

			for i in dist_list:	
				district_ids.append(str(i.id))				
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[9])				
				a_matric=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=a_matric.aggregate(Sum('school_total'))
				y=a_matric.aggregate(Sum('a_school_total'))
				m_emis+=x.values()
				m_aadhaar+=y.values()			
			# m_not_aadhaar=[i - j for i, j in zip(m_emis, m_aadhaar)]			
			a_list=zip(district_ids,district_names,m_emis,m_aadhaar)
			return render(request,'aadhaar/state/aadhaar_matric.html',locals())


class District_level_matric_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			m_b_emis=[]
			m_b_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[9])
				a_d_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_d_matric.aggregate(Sum('school_total'))
				y=a_d_matric.aggregate(Sum('a_school_total'))
				m_b_emis+=x.values()
				m_b_aadhaar+=y.values()			
			# m_b_not_aadhaar=[i - j for i, j in zip(m_b_emis, m_b_aadhaar)]			
			a_list=zip(block_ids,block_names,m_b_emis,m_b_aadhaar)
			return render(request,'aadhaar/district/district_matric_aadhaar_report.html',locals())

class Block_level_matric_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[9]).order_by('school_name')
			a_bl_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
			m_block_emis=a_bl_matric.aggregate(Sum('school_total')).values()[0]
			m_block_aadhaar=a_bl_matric.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/block_matric_aadhaar_report.html',locals())

class School_matric_aadhaar_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        
        aadhaar=aadhaar_student_count.objects.get(id=school)
               
        
        return render(request,'aadhaar/school/school_aadhar_report.html',locals())


class dee_govt_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			dee_govt_school_list=School.objects.filter(management_id__in=[1,2,3,4,5],category_id__in=[1,2,4,11,15])
			dee=aadhaar_student_count.objects.filter(school_id__in=dee_govt_school_list)
			dee_govt_emis=0
			dee_govt_aadhaar=0
			dee_govt_not_aadhaar=0
			for i in dee:
				dee_govt_emis=dee_govt_emis+i.school_total
				dee_govt_aadhaar=dee_govt_aadhaar+i.a_school_total
			dee_govt_not_aadhaar=dee_govt_emis-dee_govt_aadhaar



			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			dee_g_emis=[]
			dee_g_aadhaar=[]
						

			for i in dist_list:	
				district_ids.append(str(i.id))
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[1,2,3,4,5],category_id__in=[1,2,4,11,15])
				a_dee_g=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=a_dee_g.aggregate(Sum('school_total'))
				y=a_dee_g.aggregate(Sum('a_school_total'))
				dee_g_emis+=x.values()
				dee_g_aadhaar+=y.values()
				
			# dee_g_not_aadhaar=[i - j for i, j in zip(dee_g_emis, dee_g_aadhaar)]
			a_list=zip(district_ids,district_names,dee_g_emis,dee_g_aadhaar)
			return render(request,'aadhaar/state/aadhaar_dee_govt.html',locals())

class dee_govt_Dist_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			dee_g_blk_emis=[]
			dee_g_blk_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[1,2,3,4,5],category_id__in=[1,2,4,11,15])
				a_dee_g_blk=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_dee_g_blk.aggregate(Sum('school_total'))
				y=a_dee_g_blk.aggregate(Sum('a_school_total'))
				dee_g_blk_emis+=x.values()
				dee_g_blk_aadhaar+=y.values()			
			# dee_g_blk_not_aadhaar=[i - j for i, j in zip(dee_g_blk_emis, dee_g_blk_aadhaar)]			
			a_list=zip(block_ids,block_names,dee_g_blk_emis,dee_g_blk_aadhaar)
			return render(request,'aadhaar/district/dee_govt_dist_aadhaar_report.html',locals())


class dee_govt_block_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[1,2,3,4,5],category_id__in=[1,2,4,11,15])
			a_dee_g_blk_schl=aadhaar_student_count.objects.filter(school_id__in=school_list)
			dee_g_blk_schl_emis=a_dee_g_blk_schl.aggregate(Sum('school_total')).values()[0]
			dee_g_blk_schl_aadhaar=a_dee_g_blk_schl.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/dee_govt_block_aadhaar_report.html',locals())

class dee_govt_school_aadhaar_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        
        aadhaar=aadhaar_student_count.objects.get(id=school)
               
        
        return render(request,'aadhaar/school/dee_govt_schl_aadhaar_report.html',locals())


# -----------------Private Aided------------------
class dee_pvt_aid_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			p_a_school_list=School.objects.filter(management_id__in=[6,7],category_id__in=[1,2,4,11,15])
			pvt_aided=aadhaar_student_count.objects.filter(school_id__in=p_a_school_list)
			pvt_aided_emis=0
			pvt_aided_aadhaar=0
			pvt_aided_not_aadhaar=0
			for i in pvt_aided:
				pvt_aided_emis=pvt_aided_emis+i.school_total
				pvt_aided_aadhaar=pvt_aided_aadhaar+i.a_school_total
			pvt_aided_not_aadhaar=pvt_aided_emis-pvt_aided_aadhaar

			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			dee_pvt_aided_emis=[]
			dee_pvt_aided_aadhaar=[]
						
			for i in dist_list:	
				district_ids.append(str(i.id))
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[6,7],category_id__in=[1,2,4,11,15])
				a_dee_pvt_aided=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=a_dee_pvt_aided.aggregate(Sum('school_total'))
				y=a_dee_pvt_aided.aggregate(Sum('a_school_total'))
				dee_pvt_aided_emis+=x.values()
				dee_pvt_aided_aadhaar+=y.values()
				
			# dee_pvt_aided_not_aadhaar=[i - j for i, j in zip(dee_pvt_aided_emis,dee_pvt_aided_aadhaar)]
			a_list=zip(district_ids,district_names,dee_pvt_aided_emis,dee_pvt_aided_aadhaar)
			return render(request,'aadhaar/state/aadhaar_dee_pvt_aided.html',locals())

class dee_pvt_aided_Dist_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			dee_pvt_aid_blk_emis=[]
			dee_pvt_aid_blk_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[6,7],category_id__in=[1,2,4,11,15])
				a_dee_pvt_aid_blk=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_dee_pvt_aid_blk.aggregate(Sum('school_total'))
				y=a_dee_pvt_aid_blk.aggregate(Sum('a_school_total'))
				dee_pvt_aid_blk_emis+=x.values()
				dee_pvt_aid_blk_aadhaar+=y.values()			
			# dee_pvt_aid_blk_not_aadhaar=[i - j for i, j in zip(dee_pvt_aid_blk_emis, dee_pvt_aid_blk_aadhaar)]			
			a_list=zip(block_ids,block_names,dee_pvt_aid_blk_emis,dee_pvt_aid_blk_aadhaar)
			return render(request,'aadhaar/district/dee_pvt_aided_dist_aadhaar_report.html',locals())


class dee_pvt_aided_block_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[6,7],category_id__in=[1,2,4,11,15])
			a_dee_pvt_aid_blk_schl=aadhaar_student_count.objects.filter(school_id__in=school_list)
			dee_pvt_aid_blk_schl_aadhaar=a_dee_pvt_aid_blk_schl.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/dee_pvt_aided_block_aadhaar_report.html',locals())

class dee_pvt_aided_school_aadhaar_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        
        aadhaar=aadhaar_student_count.objects.get(id=school)
               
        return render(request,'aadhaar/school/dee_pvt_aided_schl_aadhaar_report.html',locals())


# ------------Private Unaided----------------

class dee_pvt_unaid_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			p_u_school_list=School.objects.filter(management_id__in=[8,12,13,14,15,16,17],category_id__in=[1,2,4,11,15])
			pvt_unaided=aadhaar_student_count.objects.filter(school_id__in=p_u_school_list)
			pvt_unaided_emis=0
			pvt_unaided_aadhaar=0
			pvt_unaided_not_aadhaar=0
			for i in pvt_unaided:
				pvt_unaided_emis=pvt_unaided_emis+i.school_total
				pvt_unaided_aadhaar=pvt_unaided_aadhaar+i.a_school_total
			pvt_unaided_not_aadhaar=pvt_unaided_emis-pvt_unaided_aadhaar

			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			dee_pvt_unaided_emis=[]
			dee_pvt_unaided_aadhaar=[]
					

			for i in dist_list:	
				district_ids.append(str(i.id))
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[8,12,13,14,15,16,17],category_id__in=[1,2,4,11,15])
				a_dee_pvt_unaided=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=a_dee_pvt_unaided.aggregate(Sum('school_total'))
				y=a_dee_pvt_unaided.aggregate(Sum('a_school_total'))
				dee_pvt_unaided_emis+=x.values()
				dee_pvt_unaided_aadhaar+=y.values()
				
			# dee_pvt_unaided_not_aadhaar=[i - j for i, j in zip(dee_pvt_unaided_emis,dee_pvt_unaided_aadhaar)]
			a_list=zip(district_ids,district_names,dee_pvt_unaided_emis,dee_pvt_unaided_aadhaar)
			return render(request,'aadhaar/state/aadhaar_dee_pvt_unaided.html',locals())

class dee_pvt_unaided_Dist_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			dee_pvt_unaid_blk_emis=[]
			dee_pvt_unaid_blk_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[8,12,13,14,15,16,17],category_id__in=[1,2,4,11,15])
				a_dee_pvt_unaid_blk=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_dee_pvt_unaid_blk.aggregate(Sum('school_total'))
				y=a_dee_pvt_unaid_blk.aggregate(Sum('a_school_total'))
				dee_pvt_unaid_blk_emis+=x.values()
				dee_pvt_unaid_blk_aadhaar+=y.values()			
			# dee_pvt_unaid_blk_not_aadhaar=[i - j for i, j in zip(dee_pvt_unaid_blk_emis, dee_pvt_unaid_blk_aadhaar)]			
			a_list=zip(block_ids,block_names,dee_pvt_unaid_blk_emis,dee_pvt_unaid_blk_aadhaar)
			return render(request,'aadhaar/district/dee_pvt_unaided_dist_aadhaar_report.html',locals())


class dee_pvt_unaided_block_aadhaar_report(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[8,12,13,14,15,16,17],category_id__in=[1,2,4,11,15])
			a_dee_pvt_unaid_blk_schl=aadhaar_student_count.objects.filter(school_id__in=school_list)
			dee_pvt_unaid_blk_schl_aadhaar=a_dee_pvt_unaid_blk_schl.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/dee_pvt_unaided_block_aadhaar_report.html',locals())

class dee_pvt_unaided_school_aadhaar_report(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']
        
        aadhaar=aadhaar_student_count.objects.get(id=school)
               
        return render(request,'aadhaar/school/dee_pvt_unaided_schl_aadhaar_report.html',locals())

#dse district
class dse_govt_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			dse_school_list=School.objects.filter(management_id__in= [1,2,4,5],category_id__in=[3,5,6,7,8,9,10])
			dse=aadhaar_student_count.objects.filter(school_id__in=dse_school_list)
			dse_emis=0
			dse_aadhaar=0
			dse_not_aadhaar=0
			for i in dse:
				dse_emis=dse_emis+i.school_total
				dse_aadhaar=dse_aadhaar+i.a_school_total
			dse_not_aadhaar=dse_emis-dse_aadhaar



			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			dse_g_emis=[]
			dse_g_aadhaar=[]
						

			for i in dist_list:	
				district_ids.append(str(i.id))				
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in= [1,2,4,5],category_id__in=[3,5,6,7,8,9,10])
				dse_g=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=dse_g.aggregate(Sum('school_total'))
				y=dse_g.aggregate(Sum('a_school_total'))
				dse_g_emis+=x.values()
				dse_g_aadhaar+=y.values()			
			# dse_g_not_aadhaar=[i - j for i, j in zip(dse_g_emis, dse_g_aadhaar)]			
			a_list=zip(district_ids,district_names,dse_g_emis,dse_g_aadhaar)
			return render(request,'aadhaar/state/aadhaar_dse_g_state.html',locals())


class dse_pvt_a_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			p_a_school_list=School.objects.filter(management_id__in=[6,7],category_id__in=[3,5,6,7,8,9,10])
			pvt_aided=aadhaar_student_count.objects.filter(school_id__in=p_a_school_list)
			pvt_aided_emis=0
			pvt_aided_aadhaar=0
			pvt_aided_not_aadhaar=0
			for i in pvt_aided:
				pvt_aided_emis=pvt_aided_emis+i.school_total
				pvt_aided_aadhaar=pvt_aided_aadhaar+i.a_school_total
			pvt_aided_not_aadhaar=pvt_aided_emis-pvt_aided_aadhaar


			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			dse_gpa_emis=[]
			dse_gpa_aadhar=[]
			
			
			for i in dist_list:	
				district_ids.append(str(i.id))				
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[6,7],category_id__in=[3,5,6,7,8,9,10])
				a_dse_p=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=a_dse_p.aggregate(Sum('school_total'))
				y=a_dse_p.aggregate(Sum('a_school_total'))
				dse_gpa_emis+=x.values()
				dse_gpa_aadhar+=y.values()			
			# dse_gpa_not_aadhar=[i - j for i, j in zip(dse_gpa_emis, dse_gpa_aadhar)]			
			a_list=zip(district_ids,district_names,dse_gpa_emis,dse_gpa_aadhar)
			return render(request,'aadhaar/state/aadhaar_dse_p_a_state.html',locals())

class dse_pvt_ua_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			p_u_school_list=School.objects.filter(management_id__in=[8,12,13,14,15,16,17],category_id__in=[3,5,6,7,8,9,10])
			pvt_unaided=aadhaar_student_count.objects.filter(school_id__in=p_u_school_list)
			pvt_unaided_emis=0
			pvt_unaided_aadhaar=0
			pvt_unaided_not_aadhaar=0
			for i in pvt_unaided:
				pvt_unaided_emis=pvt_unaided_emis+i.school_total
				pvt_unaided_aadhaar=pvt_unaided_aadhaar+i.a_school_total
			pvt_unaided_not_aadhaar=pvt_unaided_emis-pvt_unaided_aadhaar



			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			dse_pua_emis=[]
			dse_pua_aadhaar=[]
						

			for i in dist_list:	
				district_ids.append(str(i.id))				
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[8,12,13,14,15,16,17],category_id__in=[3,5,6,7,8,9,10])
				dse_pua=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=dse_pua.aggregate(Sum('school_total'))
				y=dse_pua.aggregate(Sum('a_school_total'))
				dse_pua_emis+=x.values()
				dse_pua_aadhaar+=y.values()			
			# dse_pua_not_aadhaar=[i - j for i, j in zip(dse_pua_emis, dse_pua_aadhaar)]			
			a_list=zip(district_ids,district_names,dse_pua_emis,dse_pua_aadhaar)#,dse_pua_not_aadhaar
			return render(request,'aadhaar/state/aadhaar_dse_p_ua_state.html',locals())

class cbse_icse_view(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			cbse_school_list=School.objects.filter(management_id__in=[10,11])
			cbse=aadhaar_student_count.objects.filter(school_id__in=cbse_school_list)
			cbse_emis=0
			cbse_aadhaar=0
			cbse_not_aadhaar=0
			for i in cbse:
				cbse_emis=cbse_emis+i.school_total
				cbse_aadhaar=cbse_aadhaar+i.a_school_total
			cbse_not_aadhaar=cbse_emis-cbse_aadhaar



			dist_list=District.objects.all().order_by('district_name')
			district_ids=[]
			district_names=[]
			cbse__emis1=[]
			cbse__aadhaar1=[]
						

			for i in dist_list:	
				district_ids.append(str(i.id))				
				district_names.append(i.district_name)
				dist=School.objects.filter(district_id=i.id,management_id__in=[10,11])
				cbse_i=aadhaar_student_count.objects.filter(school_id__in=dist)		
				x=cbse_i.aggregate(Sum('school_total'))
				y=cbse_i.aggregate(Sum('a_school_total'))
				cbse__emis1+=x.values()
				cbse__aadhaar1+=y.values()	
			# cbse__not_aadhaar=[i-j for i,j in zip(cbse__emis,cbse__aadhaar)]			
			a_list=zip(district_ids,district_names,cbse__emis1,cbse__aadhaar1)#cbse__not_aadhaar
			return render(request,'aadhaar/state/aadhaar_cbse_state.html',locals())			


#dse- block
class d_l_dse_g_aadhaar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			dse_g_b_emis=[]
			dse_g_b_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in= [1,2,4,5],category_id__in=[3,5,6,7,8,9,10])
				a_d_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_d_matric.aggregate(Sum('school_total'))
				y=a_d_matric.aggregate(Sum('a_school_total'))
				dse_g_b_emis+=x.values()
				dse_g_b_aadhaar+=y.values()			
			# dse_g_b_not_aadhaar=[i - j for i, j in zip(dse_g_b_emis, dse_g_b_aadhaar)]			
			a_list=zip(block_ids,block_names,dse_g_b_emis,dse_g_b_aadhaar)
			return render(request,'aadhaar/district/d_l_dse_govt_aadhaar.html',locals())

class d_l_dse_a_addhaar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			dse_a_b_emis=[]
			dse_a_b_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[6,7],category_id__in=[3,5,6,7,8,9,10])
				a_d_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_d_matric.aggregate(Sum('school_total'))
				y=a_d_matric.aggregate(Sum('a_school_total'))
				dse_a_b_emis+=x.values()
				dse_a_b_aadhaar+=y.values()			
			# dse_a_b_not_aadhaar=[i - j for i, j in zip(dse_a_b_emis, dse_a_b_aadhaar)]			
			a_list=zip(block_ids,block_names,dse_a_b_emis,dse_a_b_aadhaar)
			return render(request,'aadhaar/district/d_l_dse_govt_a_aadhaar.html',locals())

class d_l_dse_ua_addhaar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			dse_ua_b_emis=[]
			dse_ua_b_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[8,12,13,14,15,16,17],category_id__in=[3,5,6,7,8,9,10])
				a_d_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_d_matric.aggregate(Sum('school_total'))
				y=a_d_matric.aggregate(Sum('a_school_total'))
				dse_ua_b_emis+=x.values()
				dse_ua_b_aadhaar+=y.values()			
			# dse_ua_b_not_aadhaar=[i - j for i, j in zip(dse_ua_b_emis, dse_ua_b_aadhaar)]			
			a_list=zip(block_ids,block_names,dse_ua_b_emis,dse_ua_b_aadhaar)
			return render(request,'aadhaar/district/d_l_dse_govt_ua_aadhaar.html',locals())

class d_l_cbse_aadhaar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3]
			user=self.kwargs['pk']
			district=District.objects.get(id=user)
			blocks=Block.objects.filter(district_id=user)
			block_ids=[]
			block_names=[]
			cbse_b_emis=[]
			cbse_b_aadhaar=[]
			
			for i in blocks:
				block_ids.append(str(i.id))
				block_names.append(i.block_name)
				school_list=School.objects.filter(block_id=i.id,management_id__in=[10,11])
				a_d_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
				x=a_d_matric.aggregate(Sum('school_total'))
				y=a_d_matric.aggregate(Sum('a_school_total'))
				cbse_b_emis+=x.values()
				cbse_b_aadhaar+=y.values()			
			# cbse_b_not_aadhaar=[i - j for i, j in zip(cbse_b_emis, cbse_b_aadhaar)]			
			a_list=zip(block_ids,block_names,cbse_b_emis,cbse_b_aadhaar)
			return render(request,'aadhaar/district/d_l_cbse_aadhaar.html',locals())
#dse - block school wise

class b_l_dse_g_aadhar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in= [1,2,4,5],category_id__in=[3,5,6,7,8,9,10]).order_by('school_name')
			a_bl_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
			m_block_emis=a_bl_matric.aggregate(Sum('school_total')).values()[0]
			m_block_aadhaar=a_bl_matric.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/b_l_dse_govt_aadhar.html',locals())

class b_l_dse_a_aadhaar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[6,7],category_id__in=[3,5,6,7,8,9,10]).order_by('school_name')
			a_bl_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
			m_block_emis=a_bl_matric.aggregate(Sum('school_total')).values()[0]
			m_block_aadhaar=a_bl_matric.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/b_l_dse_govt_a_aadhar.html',locals())

class b_l_dse_ua_aadhaar(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[8,12,13,14,15,16,17],category_id__in=[3,5,6,7,8,9,10]).order_by('school_name')
			a_bl_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
			m_block_emis=a_bl_matric.aggregate(Sum('school_total')).values()[0]
			m_block_aadhaar=a_bl_matric.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/b_l_dse_govt_ua_aadhar.html',locals())

class b_l_cbse(View):
	def get(self,request,**kwargs):
		if request.user.is_authenticated():
			user_access_level=[4,3,2]
			block=self.kwargs['pk']
			block_name=Block.objects.get(id=block)
			school_list=School.objects.filter(block_id=block,management_id__in=[10,11]).order_by('school_name')
			a_bl_matric=aadhaar_student_count.objects.filter(school_id__in=school_list)
			m_block_emis=a_bl_matric.aggregate(Sum('school_total')).values()[0]
			m_block_aadhaar=a_bl_matric.aggregate(Sum('a_school_total')).values()[0]			
			return render(request,'aadhaar/block/b_l_cbse_aadhar.html',locals())



#dse school
class s_l_dse_govt_aadhaar(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']        
        aadhaar=aadhaar_student_count.objects.get(id=school)        
        return render(request,'aadhaar/school/s_l_dse_govt_aadhaar.html',locals())

class s_l_dse_a_aadhaar(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']        
        aadhaar=aadhaar_student_count.objects.get(id=school)        
        return render(request,'aadhaar/school/s_l_dse_a_aadhaar.html',locals())

class s_l_dse_ua_aadhaar(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']        
        aadhaar=aadhaar_student_count.objects.get(id=school)        
        return render(request,'aadhaar/school/s_l_dse_ua_aadhaar.html',locals())

class s_l_cbse_aadhaar(View):
    def get(self,request,**kwargs):
        user_access_level=[4,3,2,1]
        school=self.kwargs['pk']        
        aadhaar=aadhaar_student_count.objects.get(id=school)        
        return render(request,'aadhaar/school/s_l_cbse_aadhaar.html',locals())        

