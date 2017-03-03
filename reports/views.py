from django.shortcuts import render
from django.views.generic import View
from baseapp.models import *
from students.models import Child_detail,School_child_count   
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Count, Sum
from reports.models import * 
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache


class district_level_aadhaar_report(View):
    def get(self,request,**kwargs):
        
        return render(request,'aadhaar/district_login.html',locals())


class block_level_aadhaar_report(View):
    def get(self,request,**kwargs):
        
        return render(request,'aadhaar/block_login.html',locals())

# def render_to_pdf(template_src, context_dict, filename):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html = template.render(context)
#     result = StringIO.StringIO()
#     pdf = pisa.pisaDocument(
#         StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
#     if not pdf.err:
#         outfile = HttpResponse(result.getvalue(), mimetype="application/pdf")
#         outfile['Content-Disposition'] = 'attachment; filename=' + \
#             filename + '.pdf'
#         return outfile
#     return http.HttpResponse('We had some error on report generation<pre>%s</pre>' % cgi.escape(html))

# def fetch_resources(uri, rel):
#     path = os.path.join(
#         settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
#     return path

# def download_child_profile(request,ch_id):
#     child = Child_detail.objects.get(id=ch_id)
#     pagesize = 'A4'
#     title = 'Child Profile'
#     return render_to_pdf('download_child_profile.html', locals(), 'Child_Profile')

# class ReportView(View):
#     def get(self,request,**kwargs):
#         if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
#             school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
#             return render(request,'report_list.html',{'school_list':school_list})
#         elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
#             block_list = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
#             return render(request,'report_list.html',{'block_list':block_list})
#         elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
#             district_list = District.objects.all().order_by('district_name')
#             block_list = Block.objects.all().order_by('block_name')
#             return render(request,'report_list.html',{'block_list':block_list,'district_list':district_list})
#         else:
#             class_studying_list = Class_Studying.objects.all().order_by('id')
#             academic_year_list = Academic_Year.objects.all().order_by('id')
#             community_list = Community.objects.all().order_by('community_name')
#             religion_list = Religion.objects.all().order_by('religion_name')
#             language_list = Language.objects.all().order_by('language_name')
#             nationality_list = Nationality.objects.all().order_by('nationality')
#             education_medium_list = Education_medium.objects.all().order_by('education_medium')
#             diff_abled_list = Differently_abled.objects.all().order_by('da_name')
#             dis_advantagedgrp_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
#             schemes_list = Schemes.objects.all().order_by('scheme_name')
#             return render(request,'report_list.html',{'class_studying_list':class_studying_list,'academic_year_list':academic_year_list,'community_list':community_list,'religion_list':religion_list,'language_list':language_list,'nationality_list':nationality_list,'education_medium_list':education_medium_list,'diff_abled_list':diff_abled_list,'dis_advantagedgrp_list':dis_advantagedgrp_list,'schemes_list':schemes_list})
#         return render(request,'report_list.html',locals())

#     def post(self,request,**kwargs):
#         if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
#             blk1=Child_detail.objects.filter(block_id=request.user.account.associated_with).filter(academic_year_id=3).values('school').distinct()
#             school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
#             category_list=School.objects.filter(block_id=request.user.account.associated_with).filter(category__id__in=['1','2','3','6','11','12','13'])
#             print blk1
#             # print school_list
#             print category_list
#             return render(request,'report_list.html',locals())

#         elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
#             block_list1 = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
#             stud2=Child_detail.objects.filter(district_id=request.user.account.associated_with).filter(academic_year_id=3).values('block').annotate(bcount=Count('gender')).order_by('block')
#             stud3=Child_detail.objects.filter(district_id=request.user.account.associated_with).filter(academic_year_id=3).values('block').annotate(scount=Count('staff_id', distinct=True)).order_by('block')
#             stud4=School.objects.filter(district_id=request.user.account.associated_with).values('block').annotate(schcount=Count('school_code', distinct=True)).order_by('block')
#             return render(request,'report_list.html',locals())
#         elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
#             district_list = District.objects.all().order_by('district_name')
#             dist1=Child_detail.objects.filter(academic_year_id=3).values('district').annotate(bcount=Count('gender')).order_by('district')
#             dist2=Child_detail.objects.filter(academic_year_id=3).values('district').annotate(scount=Count('staff_id', distinct=True)).order_by('district')
#             dist3=School.objects.values('district').annotate(schcount=Count('school_code', distinct=True)).order_by('district')
#             return render(request,'report_list.html',locals())
#         else:
#             school_id = request.user.account.associated_with
#             community_list = Community.objects.all().order_by('community_name')
#             sub_caste_list = Sub_Castes.objects.all().order_by('caste_name')
#             religion_list = Religion.objects.all().order_by('religion_name')
#             language_list = Language.objects.all().order_by('language_name')
#             nationality_list = Nationality.objects.all().order_by('nationality')
#             education_medium_list = Education_medium.objects.all().order_by('education_medium')
#             diff_abled_list = Differently_abled.objects.all().order_by('da_name')
#             dis_advantagedgrp_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
#             schemes_list = Schemes.objects.all().order_by('scheme_name')
#             cur1 = connection.cursor()
#             cur2 = connection.cursor()
#             cur3 = connection.cursor()
#             cur4 = connection.cursor()
#             cur5 = connection.cursor()
#             cur6 = connection.cursor()
#             cur7 = connection.cursor()
           
#             kwargs = {}
#             kwargs["school_id"] = eval(school_id)
#             student_detail_list = Child_detail.objects.filter(**kwargs)
#             if 'class_studying_id' in request.POST:
#                 kwargs['class_studying_id__in'] = request.POST.getlist("class_studying_id")
#             else:
#                 pass
#             if 'class_section' in request.POST:
#                 kwargs["class_section__in"] = request.POST.getlist("class_section") 
#             else:
#                 pass
#             if 'academic_year_id' in request.POST:
#                 kwargs["academic_year_id__in"] = request.POST.getlist("academic_year_id")
#             else:
#                 pass
#             if 'gender' in request.POST:
#                 kwargs["gender__in"] = request.POST.getlist("gender")
#             else:
#                 pass
#             if 'community_id' in request.POST:
#                 kwargs["community_id__in"] = request.POST.getlist("community_id")
#             else:
#                 pass
#             if 'religion_id' in request.POST:
#                 kwargs["religion_id__in"] =request.POST.getlist("religion_id")
#             else:
#                 pass
#             if 'mothertounge_id' in request.POST:
#                 kwargs["mothertounge_id__in"] =request.POST.getlist("mothertounge_id")
#             else:
#                 pass
#             if 'child_differently_abled' in request.POST:
#                 kwargs["child_differently_abled__in"] =request.POST.getlist("child_differently_abled")
#             else:
#                 pass
#             if 'child_disadvantaged_group' in request.POST:
#                 kwargs["child_disadvantaged_group__in"] =request.POST.getlist("child_disadvantaged_group")
#             else:
#                 pass
#             if 'nationality_id' in request.POST:
#                 kwargs["nationality_id__in"] =request.POST.getlist("nationality_id")
#             else:
#                 pass
#             if 'blood_group' in request.POST:
#                 kwargs["blood_group__in"] =request.POST.getlist("blood_group")
#             else:
#                 pass
#             if 'mother_occupation' in request.POST:
#                 kwargs["mother_occupation__in"] =request.POST.getlist("mother_occupation")
#             else:
#                 pass
#             if 'father_occupation' in request.POST:
#                 kwargs["father_occupation__in"] =request.POST.getlist("father_occupation")
#             else:
#                 pass
#             if 'attendance_status' in request.POST:
#                 kwargs["attendance_status__in"] =request.POST.getlist("attendance_status")
#             else:
#                 pass
#             if 'education_medium_id' in request.POST:
#                 kwargs["education_medium_id__in"] =request.POST.getlist("education_medium_id")
#             else:
#                 pass
#             if 'govt_schemes_status' in request.POST:
#                 kwargs["govt_schemes_status__in"] =request.POST.getlist("govt_schemes_status")
#             else:
#                 pass
#             if 'child_status' in request.POST:
#                 kwargs["child_status__in"] =request.POST.getlist("child_status")
#             else:
#                 pass
#             student_detail_list = Child_detail.objects.filter(**kwargs)
#             student_detail_count = student_detail_list.count()
#             paginator = Paginator(student_detail_list, 10)
#             page = request.GET.get('page')
#             try:
#                 page_obj = paginator.page(page)
#             except PageNotAnInteger:
#                 # If page is not an integer, deliver first page.
#                 page_obj = paginator.page(1)
#             except EmptyPage:
#                 # If page is out of range (e.g. 9999), deliver last page of results.
#                 page_obj = paginator.page(paginator.num_pages)
#             return render(request,'report_list.html',locals())
#             # return render_to_pdf('download_child_profile.html',locals(),'Child_Profile')
#         pagesize = 'A4'
#         title = 'Child Profile'
#         return render(request,'report_list.html',locals())
class aadhaar_report(View):
    def get(self,request,**kwargs):
        
        return render(request,'aadhaar/base.html',locals())

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

