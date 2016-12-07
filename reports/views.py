from django.shortcuts import render
from django.views.generic import View
from baseapp.models import *
from students.models import Child_detail    
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Count, Sum




def render_to_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(
        StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
    if not pdf.err:
        outfile = HttpResponse(result.getvalue(), mimetype="application/pdf")
        outfile['Content-Disposition'] = 'attachment; filename=' + \
            filename + '.pdf'
        return outfile
    return http.HttpResponse('We had some error on report generation<pre>%s</pre>' % cgi.escape(html))

def fetch_resources(uri, rel):
    path = os.path.join(
        settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path

def download_child_profile(request,ch_id):
    child = Child_detail.objects.get(id=ch_id)
    pagesize = 'A4'
    title = 'Child Profile'
    return render_to_pdf('download_child_profile.html', locals(), 'Child_Profile')

class ReportView(View):
    def get(self,request,**kwargs):
        if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
            school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
            return render(request,'report_list.html',{'school_list':school_list})
        elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
            block_list = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
            return render(request,'report_list.html',{'block_list':block_list})
        elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
            district_list = District.objects.all().order_by('district_name')
            block_list = Block.objects.all().order_by('block_name')
            return render(request,'report_list.html',{'block_list':block_list,'district_list':district_list})
        else:
            class_studying_list = Class_Studying.objects.all().order_by('id')
            academic_year_list = Academic_Year.objects.all().order_by('id')
            community_list = Community.objects.all().order_by('community_name')
            religion_list = Religion.objects.all().order_by('religion_name')
            language_list = Language.objects.all().order_by('language_name')
            nationality_list = Nationality.objects.all().order_by('nationality')
            education_medium_list = Education_medium.objects.all().order_by('education_medium')
            diff_abled_list = Differently_abled.objects.all().order_by('da_name')
            dis_advantagedgrp_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
            schemes_list = Schemes.objects.all().order_by('scheme_name')
            return render(request,'report_list.html',{'class_studying_list':class_studying_list,'academic_year_list':academic_year_list,'community_list':community_list,'religion_list':religion_list,'language_list':language_list,'nationality_list':nationality_list,'education_medium_list':education_medium_list,'diff_abled_list':diff_abled_list,'dis_advantagedgrp_list':dis_advantagedgrp_list,'schemes_list':schemes_list})
        return render(request,'report_list.html',locals())

    def post(self,request,**kwargs):
        if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
            blk1=Child_detail.objects.filter(block_id=request.user.account.associated_with).filter(academic_year_id=3).values('school').distinct()
            school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
            category_list=School.objects.filter(block_id=request.user.account.associated_with).filter(category__id__in=['1','2','3','6','11','12','13'])
            print blk1
            # print school_list
            print category_list
            return render(request,'report_list.html',locals())

        elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
            block_list1 = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
            stud2=Child_detail.objects.filter(district_id=request.user.account.associated_with).filter(academic_year_id=3).values('block').annotate(bcount=Count('gender')).order_by('block')
            stud3=Child_detail.objects.filter(district_id=request.user.account.associated_with).filter(academic_year_id=3).values('block').annotate(scount=Count('staff_id', distinct=True)).order_by('block')
            stud4=School.objects.filter(district_id=request.user.account.associated_with).values('block').annotate(schcount=Count('school_code', distinct=True)).order_by('block')
            return render(request,'report_list.html',locals())
        elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
            district_list = District.objects.all().order_by('district_name')
            dist1=Child_detail.objects.filter(academic_year_id=3).values('district').annotate(bcount=Count('gender')).order_by('district')
            dist2=Child_detail.objects.filter(academic_year_id=3).values('district').annotate(scount=Count('staff_id', distinct=True)).order_by('district')
            dist3=School.objects.values('district').annotate(schcount=Count('school_code', distinct=True)).order_by('district')
            return render(request,'report_list.html',locals())
        else:
            school_id = request.user.account.associated_with
            community_list = Community.objects.all().order_by('community_name')
            sub_caste_list = Sub_Castes.objects.all().order_by('caste_name')
            religion_list = Religion.objects.all().order_by('religion_name')
            language_list = Language.objects.all().order_by('language_name')
            nationality_list = Nationality.objects.all().order_by('nationality')
            education_medium_list = Education_medium.objects.all().order_by('education_medium')
            diff_abled_list = Differently_abled.objects.all().order_by('da_name')
            dis_advantagedgrp_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
            schemes_list = Schemes.objects.all().order_by('scheme_name')
            cur1 = connection.cursor()
            cur2 = connection.cursor()
            cur3 = connection.cursor()
            cur4 = connection.cursor()
            cur5 = connection.cursor()
            cur6 = connection.cursor()
            cur7 = connection.cursor()
           
            kwargs = {}
            kwargs["school_id"] = eval(school_id)
            student_detail_list = Child_detail.objects.filter(**kwargs)
            if 'class_studying_id' in request.POST:
                kwargs['class_studying_id__in'] = request.POST.getlist("class_studying_id")
            else:
                pass
            if 'class_section' in request.POST:
                kwargs["class_section__in"] = request.POST.getlist("class_section") 
            else:
                pass
            if 'academic_year_id' in request.POST:
                kwargs["academic_year_id__in"] = request.POST.getlist("academic_year_id")
            else:
                pass
            if 'gender' in request.POST:
                kwargs["gender__in"] = request.POST.getlist("gender")
            else:
                pass
            if 'community_id' in request.POST:
                kwargs["community_id__in"] = request.POST.getlist("community_id")
            else:
                pass
            if 'religion_id' in request.POST:
                kwargs["religion_id__in"] =request.POST.getlist("religion_id")
            else:
                pass
            if 'mothertounge_id' in request.POST:
                kwargs["mothertounge_id__in"] =request.POST.getlist("mothertounge_id")
            else:
                pass
            if 'child_differently_abled' in request.POST:
                kwargs["child_differently_abled__in"] =request.POST.getlist("child_differently_abled")
            else:
                pass
            if 'child_disadvantaged_group' in request.POST:
                kwargs["child_disadvantaged_group__in"] =request.POST.getlist("child_disadvantaged_group")
            else:
                pass
            if 'nationality_id' in request.POST:
                kwargs["nationality_id__in"] =request.POST.getlist("nationality_id")
            else:
                pass
            if 'blood_group' in request.POST:
                kwargs["blood_group__in"] =request.POST.getlist("blood_group")
            else:
                pass
            if 'mother_occupation' in request.POST:
                kwargs["mother_occupation__in"] =request.POST.getlist("mother_occupation")
            else:
                pass
            if 'father_occupation' in request.POST:
                kwargs["father_occupation__in"] =request.POST.getlist("father_occupation")
            else:
                pass
            if 'attendance_status' in request.POST:
                kwargs["attendance_status__in"] =request.POST.getlist("attendance_status")
            else:
                pass
            if 'education_medium_id' in request.POST:
                kwargs["education_medium_id__in"] =request.POST.getlist("education_medium_id")
            else:
                pass
            if 'govt_schemes_status' in request.POST:
                kwargs["govt_schemes_status__in"] =request.POST.getlist("govt_schemes_status")
            else:
                pass
            if 'child_status' in request.POST:
                kwargs["child_status__in"] =request.POST.getlist("child_status")
            else:
                pass
            student_detail_list = Child_detail.objects.filter(**kwargs)
            student_detail_count = student_detail_list.count()
            paginator = Paginator(student_detail_list, 10)
            page = request.GET.get('page')
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page_obj = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                page_obj = paginator.page(paginator.num_pages)
            return render(request,'report_list.html',locals())
            # return render_to_pdf('download_child_profile.html',locals(),'Child_Profile')
        pagesize = 'A4'
        title = 'Child Profile'
        return render(request,'report_list.html',locals())
