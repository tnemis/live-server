from django.views.generic import *
from django.contrib import messages
from forms import Child_detailform
from baseapp.forms import Pool_databaseform
from django.shortcuts import *
from students.models import *
from django.db.models import *
from baseapp.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger
from datetime import *
from django import template
from django.contrib import messages
from excel_response import ExcelResponse
from django.utils import simplejson
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.db.models import *
from datetime import datetime
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.conf import settings
import ho.pisa as pisa
import cStringIO as StringIO
import cgi


        
class Nominal_roll_checklist(View):
    def get(self,request,**kwargs):
        pk=self.kwargs.get('pk')
        school_id = request.user.account.associated_with
        school=School.objects.get(id=school_id)
        kwargs={}
        kwargs['school_id']=school_id
        kwargs['class_studying']=pk
        nominal_roll_list=Child_detail.objects.filter(**kwargs).filter(transfer_flag__in=[0,2]).order_by('group_code')
        return render(request,'students/child_detail/nominal_roll_print.html',locals())
        
# class Nominal_roll_checklist(View):
#     def get(self,request,**kwargs):
#         pk=self.kwargs.get('pk')
#         school_id = request.user.account.associated_with
#         school=School.objects.get(id=school_id)
#         kwargs={}
#         kwargs['school_id']=school_id
#         kwargs['class_studying']=pk
#         students=Child_detail.objects.filter(**kwargs).filter(transfer_flag__in=[0,2]).order_by('group_code')
#         file_name='Nominal_roll_check_list_2017'
#         filename = str(file_name)
#         response = HttpResponse(content_type='application/pdf')
#         photo=settings.MEDIA_URL
#         static=settings.STATIC_URL
#         response['Content-Disposition'] = 'attachement; filename={0}.pdf'.format(filename)
#         pdf=create_pdf(
#             'students/child_detail/nominal_roll_checklist.html',
#                     {   
#                         'STATIC_URL':static,
#                         'MEDIA_URL':photo,   
#                         'nominal_roll_list':chunks,
#                         'school':school,
#                         'pagesize':'A4',
#                         'class':pk,
#                     }
#                 )
#         response.write(pdf)
#         return response
        
def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path

def create_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=fetch_resources )
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


# class Nominal_roll_list(View):
#     def get(self,request,**kwargs):
#         pk=self.kwargs.get('pk')
#         school_code = self.kwargs.get('school_code')
#         school_id = request.user.account.associated_with
#         schl_id = School.objects.get(id=school_id)
#         class_students=Child_detail.objects.filter(school_id=school_id,transfer_flag__in=[0,2],class_studying=pk)
#         child_detail_list = class_students.values("name","aadhaar_eid_number","aadhaar_uid_number","gender","dob","community__community_name","religion__religion_name","mothertounge__language_name","phone_number","child_differently_abled","differently_abled","child_disadvantaged_group","disadvantaged_group","subcaste__caste_name","nationality__nationality","house_address","native_district","pin_code","blood_group","mother_name","mother_occupation","father_name","father_occupation","parent_income","class_studying__class_studying","group_code__group_code","group_code__group_name","attendance_status","sport_participation","education_medium__education_medium","district__district_name","block__block_name","unique_id_no","school_id","staff_id","bank__bank","bank_account_no","schemes","academic_year__academic_year","transfer_flag","transfer_date","name_tamil","class_section","student_admitted_section","school_admission_no","bank_ifsc_code","sports_player","sports_name","community_certificate","child_status","height","weight","laptop_issued","laptop_slno","guardian_name",'grpcode_language1','grpcode_language2','grpcode_language3','grpcode_language4','first_language','optional_language','sci_practical','lang_exemption','lang_exemption1','first_language','da_id_no')
#         udise=schl_id.school_code
#         if pk == '12':
#             data = [[udise],
#             ['S.no',
#             'Unique Id',
#             'Name', 
#             'Gender', 
#             'DoB', 
#             'Differently_abled',
#             'Differently_abled_name',
#             'Differently_abled_id',
#             'Religion',
#             'Community', 
#             'Subcaste',
#             'Class',
#             'Section',
#             'Aadhaar',
#             'Father name',
#             'Mother name',
#             'Mobile',
#             'First_lang',
#             'GROUP_CODE_NO',
#             'GROUP_CODE',
#             'GROUP_CODE_LANG_1',
#             'GROUP_CODE_LANG_2',
#             'GROUP_CODE_LANG_3',
#             'GROUP_CODE_LANG_4',
#             'Lang_exmp',
            
#             ]]
#             S_No=0
#             for i in child_detail_list:
#                 S_No+=1
#                 data.append([S_No,
#                     str(i['unique_id_no']),
#                     i['name'], 
#                     i['gender'],
#                     i['dob'],
#                     i['child_differently_abled'],
#                     i['differently_abled'],
#                     i['da_id_no'],
#                     i['religion__religion_name'], 
#                     i['community__community_name'], 
#                     i['subcaste__caste_name'],
#                     i['class_studying__class_studying'],
#                     i['class_section'],
#                     i['aadhaar_uid_number'],
#                     i['father_name'],
#                     i['mother_name'],
#                     i['phone_number'],
#                     i['first_language'],
#                     i['group_code__group_code'],
#                     i['group_code__group_name'],
#                     i['grpcode_language1'],
#                     i['grpcode_language2'],
#                     i['grpcode_language3'],
#                     i['grpcode_language4'],
#                     i['lang_exemption1'],
                    
#                     ])
#             return ExcelResponse(data, 'HS_Nominal_roll_list',)

#         if pk == '10':
#             data = [[udise],
#             ['S.no',
#             'Unique Id',
#             'Name', 
#             'Gender', 
#             'DoB', 
#             'Differently_abled',
#             'Differently_abled_name',
#             'Differently_abled_id',
#             'Religion',
#             'Community', 
#             'Subcaste',
#             'Class',
#             'Section',
#             'Aadhaar',
#             'Father name',
#             'Mother name',
#             'Mobile',
#             'Part IV optional language',
#             'Lang_exmp',
#             'SSLC_SCIENCE_PRAC_EXP']]
#             S_No=0
#             for i in child_detail_list:
#                 S_No+=1
#                 data.append([S_No,
#                     str(i['unique_id_no']),
#                     i['name'], 
#                     i['gender'],
#                     i['dob'],
#                     i['child_differently_abled'],
#                     i['differently_abled'],
#                     i['da_id_no'],
#                     i['religion__religion_name'], 
#                     i['community__community_name'], 
#                     i['subcaste__caste_name'],
#                     i['class_studying__class_studying'],
#                     i['class_section'],
#                     i['aadhaar_uid_number'],
#                     i['father_name'],
#                     i['mother_name'],
#                     i['phone_number'],
#                     i['optional_language'],
#                     i['lang_exemption'],
#                     i['sci_practical']

#                     ])
#             return ExcelResponse(data, 'SSLC_Nominal_roll_list')



class Nominal_roll_list_10(View):
    def get(self,request,**kwargs):
        import xlwt
        response = HttpResponse(mimetype='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=SSLC_Nominal_roll_list.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Child_detail")
        school_id = request.user.account.associated_with
        class_students=Child_detail.objects.filter(school_id=school_id,transfer_flag__in=[0,2],class_studying=10)
        child_detail_list = class_students.values("name","aadhaar_eid_number","aadhaar_uid_number","gender","dob","community__community_name","religion__religion_name","mothertounge__language_name","phone_number","child_differently_abled","differently_abled","child_disadvantaged_group","disadvantaged_group","subcaste__caste_name","nationality__nationality","house_address","native_district","pin_code","blood_group","mother_name","mother_occupation","father_name","father_occupation","parent_income","class_studying__class_studying","group_code__group_code","group_code__group_name","attendance_status","sport_participation","education_medium__education_medium","district__district_name","block__block_name","unique_id_no","school_id","staff_id","bank__bank","bank_account_no","schemes","academic_year__academic_year","transfer_flag","transfer_date","name_tamil","class_section","student_admitted_section","school_admission_no","bank_ifsc_code","sports_player","sports_name","community_certificate","child_status","height","weight","laptop_issued","laptop_slno","guardian_name",'grpcode_language1','grpcode_language2','grpcode_language3','grpcode_language4','first_language','optional_language','sci_practical','lang_exemption','lang_exemption1','first_language','da_id_no')
        row_no = 0
        columns = [
            (u"S.NO",1000),
            (u"Unique Id",5000),
            (u"Name",6000), 
            (u"Gender",3000), 
            (u"DoB",3000), 
            (u"Differently_abled",2000),
            (u"Differently_abled_name",7000),
            (u"Differently_abled_id",4000),
            (u"Religion",4000),
            (u"Community",4000), 
            (u"Subcaste",4000),
            (u"Class",2000),
            (u"Section",2000),
            (u"Aadhaar",5000),
            (u"Father name",4000),
            (u"Mother name",4000),
            (u"Mobile",3000),
            (u"Part IV optional language",4000),
            (u"Lang_exmp",4000),
            (u"SSLC_SCIENCE_PRAC_EXP",4000)
        ]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in xrange(len(columns)):
            ws.write(row_no, col_num, columns[col_num][0], font_style)
            ws.col(col_num).width = columns[col_num][1]
        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1
        for obj in child_detail_list:
            row_no += 1
            row = [row_no,
                    str(obj['unique_id_no']),
                    obj['name'], 
                    obj['gender'],
                    str(obj['dob']),
                    obj['child_differently_abled'],
                    obj['differently_abled'],
                    obj['da_id_no'],
                    obj['religion__religion_name'], 
                    obj['community__community_name'], 
                    obj['subcaste__caste_name'],
                    obj['class_studying__class_studying'],
                    obj['class_section'],
                    obj['aadhaar_uid_number'],
                    obj['father_name'],
                    obj['mother_name'],
                    obj['phone_number'],
                    obj['optional_language'],
                    obj['lang_exemption'],
                    obj['sci_practical']
            ]
            for col_num in xrange(len(row)):
                ws.write(row_no, col_num, row[col_num], font_style)           
        wb.save(response)
        return response   
        export_xls.short_description = u"Export XLS"  

class Nominal_roll_list_12(View):
    def get(self,request,**kwargs):
        import xlwt
        response = HttpResponse(mimetype='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=HSC_Nominal_roll_list.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Child_detail")
        school_id = request.user.account.associated_with
        class_students=Child_detail.objects.filter(school_id=school_id,transfer_flag__in=[0,2],class_studying=12)
        child_detail_list = class_students.values("name","aadhaar_eid_number","aadhaar_uid_number","gender","dob","community__community_name","religion__religion_name","mothertounge__language_name","phone_number","child_differently_abled","differently_abled","child_disadvantaged_group","disadvantaged_group","subcaste__caste_name","nationality__nationality","house_address","native_district","pin_code","blood_group","mother_name","mother_occupation","father_name","father_occupation","parent_income","class_studying__class_studying","group_code__group_code","group_code__group_name","attendance_status","sport_participation","education_medium__education_medium","district__district_name","block__block_name","unique_id_no","school_id","staff_id","bank__bank","bank_account_no","schemes","academic_year__academic_year","transfer_flag","transfer_date","name_tamil","class_section","student_admitted_section","school_admission_no","bank_ifsc_code","sports_player","sports_name","community_certificate","child_status","height","weight","laptop_issued","laptop_slno","guardian_name",'grpcode_language1','grpcode_language2','grpcode_language3','grpcode_language4','first_language','optional_language','sci_practical','lang_exemption','lang_exemption1','first_language','da_id_no')
        row_no = 0
        columns = [
            (u"S.no",1000),
            (u"Unique Id",6000),
            (u"Name'",6000) ,
            (u"Gender'",3000),
            (u"Dob",4000), 
            (u"Differently_abled",5000),
            (u"Differently_abled_name",5000),
            (u"Differently_abled_id",5000),
            (u"Religion",5000),
            (u"Community",5000), 
            (u"Subcaste",5000),
            (u"Class",3000),
            (u"Section",3000),
            (u"Aadhaar",5000),
            (u"Father name",5000),
            (u"Mother name",5000),
            (u"Mobile",5000),
            (u"First_lang",3000),
            (u"GROUP_CODE_NO",2000),
            (u"GROUP_CODE",7000),
            (u"GROUP_CODE_LANG_1",3000),
            (u"GROUP_CODE_LANG_2",3000),
            (u"GROUP_CODE_LANG_3",3000),
            (u"GROUP_CODE_LANG_4",3000),
            (u"Lang_exmp",3000)
        ]
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col_num in xrange(len(columns)):
            ws.write(row_no, col_num, columns[col_num][0], font_style)
            ws.col(col_num).width = columns[col_num][1]
        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1
        for objects in child_detail_list:
            row_no += 1
            row = [row_no,
                    str(objects['unique_id_no']),
                    objects['name'], 
                    objects['gender'],
                    str(objects['dob']),
                    objects['child_differently_abled'],
                    objects['differently_abled'],
                    objects['da_id_no'],
                    objects['religion__religion_name'], 
                    objects['community__community_name'], 
                    objects['subcaste__caste_name'],
                    objects['class_studying__class_studying'],
                    objects['class_section'],
                    str(objects['aadhaar_uid_number']),
                    objects['father_name'],
                    objects['mother_name'],
                    objects['phone_number'],
                    objects['first_language'],
                    objects['group_code__group_code'],
                    objects['group_code__group_name'],
                    objects['grpcode_language1'],
                    objects['grpcode_language2'],
                    objects['grpcode_language3'],
                    objects['grpcode_language4'],
                    objects['lang_exemption1']
            ]
            for col_num in xrange(len(row)):
                ws.write(row_no, col_num, row[col_num], font_style)           
        wb.save(response)
        return response   
        export_xls.short_description = u"Export XLS"  