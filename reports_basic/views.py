from django.shortcuts import render
from django.views.generic import View
from baseapp.models import School,Block,Class_Studying,Academic_Year,District
from students.models import Child_detail	
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, PageNotAnInteger




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


class ReportViewBasic(View):
    def get(self,request,**kwargs):
        if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
            school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
            return render(request,'report_list_basic.html',{'school_list':school_list})
        elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
            block_list = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
            school_list = School.objects.filter(district_id=request.user.account.associated_with).order_by('school_name')
            return render(request,'report_list_basic.html',{'school_list':school_list,'block_list':block_list})
        elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
            district_list = District.objects.all().order_by('district_name')
            block_list = Block.objects.all().order_by('block_name')
            school_list = School.objects.all().order_by('school_name')
            return render(request,'report_list_basic.html',{'school_list':school_list,'block_list':block_list,'district_list':district_list})
        return render(request,'report_list_basic.html',locals())
    
    def post(self,request,**kwargs):
        if request.POST["class_studying"] == "all":
            class_studying=request.POST["class_studying"]
        if request.POST["class_studying"] == "all":
            academic_year=request.POST["academic_year"]
        if request.user.account.user_category_id == 2 or request.user.account.user_category_id == 5:
            school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
            school_id = request.POST["school_list"]
            if request.POST["class_studying"] == 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(school_id=request.POST["school_list"])
            elif request.POST["class_studying"] != 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(school_id=request.POST["school_list"],class_studying=request.POST["class_studying"])
            elif request.POST["class_studying"] == 'all' and request.POST["academic_year"] != 'all':
                student_detail = Child_detail.objects.filter(school_id=request.POST["school_list"],academic_year_id=request.POST["academic_year"])
            else:
                student_detail = Child_detail.objects.filter(school_id=request.POST["school_list"],class_studying=request.POST["class_studying"],academic_year_id=request.POST["academic_year"])
            return render_to_pdf('download_child_profile_basic.html',locals(),'Child_Profile')

        elif request.user.account.user_category_id == 3 or request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
            block_list = Block.objects.filter(district_id=request.user.account.associated_with).order_by('block_name')
            school_list = School.objects.filter(district_id=request.user.account.associated_with).order_by('school_name')
            school_id = request.POST["school_list"]
            block_id = request.POST["block_list"]
            if request.POST["class_studying"] == 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"])
            elif request.POST["class_studying"] != 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"],class_studying=request.POST["class_studying"])
            elif request.POST["class_studying"] == 'all' and request.POST["academic_year"] != 'all':
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"],academic_year_id=request.POST["academic_year"])
            else:
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"],class_studying=request.POST["class_studying"],academic_year_id=request.POST["academic_year"])
            return render_to_pdf('download_child_profile_basic.html',locals(),'Child_Profile')
        elif request.user.account.user_category_id == 4 or request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17:
            district_list = District.objects.all().order_by('district_name')
            block_list = Block.objects.all().order_by('block_name')
            school_list = School.objects.all().order_by('school_name')
            school_id = request.POST["school_list"]
            block_id = request.POST["block_list"]
            district_id = request.POST["district_list"]
            if request.POST["class_studying"] == 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"])
            elif request.POST["class_studying"] != 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"],class_studying=request.POST["class_studying"])
            elif request.POST["class_studying"] == 'all' and request.POST["academic_year"] != 'all':
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"],academic_year_id=request.POST["academic_year"])
            else:
                student_detail = Child_detail.objects.filter(block_id = request.POST["block_list"],school_id=request.POST["school_list"],class_studying=request.POST["class_studying"],academic_year_id=request.POST["academic_year"])
            return render_to_pdf('download_child_profile_basic.html',locals(),'Child_Profile')
        else:
            school_id = request.user.account.associated_with
            if request.POST["class_studying"] == 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(school_id=school_id)
            elif request.POST["class_studying"] != 'all' and request.POST["academic_year"] == 'all':
                student_detail = Child_detail.objects.filter(school_id=school_id,class_studying=request.POST["class_studying"])
            elif request.POST["class_studying"] == 'all' and request.POST["academic_year"] != 'all':
                student_detail = Child_detail.objects.filter(school_id=school_id,academic_year_id=request.POST["academic_year"])
            else:
                student_detail = Child_detail.objects.filter(school_id=school_id,class_studying=request.POST["class_studying"],academic_year_id=request.POST["academic_year"])
                cls_stud = Class_Studying.objects.get(id=request.POST["class_studying"])
                class_study = cls_stud.class_studying
                acad_yr = Academic_Year.objects.get(id=request.POST["academic_year"])
                aca_year = acad_yr.academic_year
            schl_name = School.objects.get(id=school_id)
            school_name = schl_name.school_name
            
            return render_to_pdf('download_child_profile_basic.html',locals(),'Child_Profile')
        pagesize = 'A4'
        title = 'Child Profile'
        return render(request,'report_list_basic.html',locals())
