from django.views.generic import View,ListView, DetailView, CreateView, \
    DeleteView, UpdateView, \
    ArchiveIndexView, DateDetailView, \
    DayArchiveView, MonthArchiveView, \
    TodayArchiveView, WeekArchiveView, \
    YearArchiveView
from django.contrib import messages
from forms import Child_detailform
from baseapp.forms import Pool_databaseform
from django.shortcuts import render
from students.models import Child_detail, Child_family_detail, School_child_count, Parent_annual_income
from django.db.models import Q
from baseapp.models import State, District, School, Habitation, Zone, Schemes, Class_Studying, Differently_abled, Disadvantaged_group, Child_detail_pool_database, Language, Group_code, Bank, Education_medium, Nationality, Religion, Community,Sub_Castes
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger
from datetime import datetime
from django import template
from django.contrib import messages
from excel_response import ExcelResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Child_detailView(object):
    model = Child_detail

    @method_decorator(login_required)
    def get_template_names(self):
        """Nest templates within child_detail directory."""
        tpl = super(Child_detailView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'child_detail'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Child_detailDateView(Child_detailView):
    date_field = 'dob'
    month_format = '%m'


class Child_detailBaseListView(Child_detailView):
    paginate_by = 10


class Child_detailArchiveIndexView(
        Child_detailDateView, Child_detailBaseListView, ArchiveIndexView):

    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailCreateView(View):
    @method_decorator(login_required)
    def get(self,request,**kwargs):
        form=Child_detailform()
        district_list = District.objects.all().exclude(district_name='None').order_by('district_name')
        differently_abled_list = Differently_abled.objects.all().order_by('da_name')
        dis_advantaged_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
        language_list = Language.objects.all().exclude(language_name='Undefined').order_by('language_name')
        education_medium_list = Education_medium.objects.all().exclude(education_medium='Undefined').order_by('education_medium')
        religion_list = Religion.objects.all().exclude(religion_name='Undefined').order_by('id')
        community_list = Community.objects.all().exclude(community_name='undefined').order_by('id')
        schemes = Schemes.objects.all().order_by('scheme_name')
        class_studying_list = Class_Studying.objects.all()
        nationality_list = Nationality.objects.all().exclude(nationality='Undefined').order_by('id')
        group_code_list = Group_code.objects.all()
        bank_list = Bank.objects.all()
        state_list = State.objects.all().order_by('state_name')
        parent_income_list = Parent_annual_income.objects.all().order_by('id')
        govt_aid_school_management_list = [1,2,3,4,5,6,7]
        aid_school_management_list = [6,7]
        private_school_management_list = [8,9,10,11,12,13,14,15,16,17,18]
        return render (request,'students/child_detail/child_detail_form.html',{'form':form,'district_list':district_list,'schemes':schemes,'differently_abled_list':differently_abled_list,'dis_advantaged_list':dis_advantaged_list,'language_list':language_list,'class_studying_list':class_studying_list,'group_code_list':group_code_list,'bank_list':bank_list,'state_list':state_list,'parent_income_list':parent_income_list,'govt_aid_school_management_list':govt_aid_school_management_list,'aid_school_management_list':aid_school_management_list,'education_medium_list':education_medium_list,'nationality_list':nationality_list,'religion_list':religion_list,'community_list':community_list,'private_school_management_list':private_school_management_list})

    @method_decorator(login_required)
    def post(self,request,**kwargs):
        # import ipdb
        # ipdb.set_trace()
        form = Child_detailform(request.POST,request.FILES)
        if form.is_valid():
            # if form.cleaned_data["disadvantaged_group"]:
            #     dis_group_list=request.POST.getlist('disadvantaged_group')
            #     dis_group_lst=''
            #     for group in dis_group_list:
            #         dis_group_lst=dis_group_lst+group+','
            # else:
            #     dis_group_lst = form.cleaned_data["disadvantaged_group"]

            if form.cleaned_data['schemes']:
                scheme_list=request.POST.getlist('schemes')
                scheme_lst=''
                for scheme in scheme_list:
                    scheme_lst=scheme_lst+scheme+','
            else:
                scheme_lst = form.cleaned_data['schemes']

            # if form.cleaned_data['house_address']:
            #     address_detail = request.POST.getlist('house_address')
            #     address=''
            #     for adrs in address_detail:
            #         address=address+adrs+','
            # else:
            #     address = form.cleaned_data['house_address']

            if form.cleaned_data['nutritious_meal_flag'] == "Yes":
                nutritious_meal_flag = 1
            else:
                nutritious_meal_flag = 0

            if form.cleaned_data['community_certificate'] == "Yes":
                comm_certificate_no = form.cleaned_data['community_certificate_no']
                comm_certificate_date = form.cleaned_data['community_certificate_date']             
            else:
                comm_certificate_no = ''
                comm_certificate_date = '1111-11-11'


            child = Child_detail(
                name = form.cleaned_data['name'],
                name_tamil = form.cleaned_data['name_tamil'],
                aadhaar_id = form.cleaned_data['aadhaar_id'],
                aadhaar_uid_number = form.cleaned_data['aadhaar_uid_number'],
                photograph = form.cleaned_data['photograph'],
                photo = form.cleaned_data['photograph'],
                gender = form.cleaned_data['gender'],
                dob = form.cleaned_data['dob'],
                community = form.cleaned_data['community'],
                community_certificate = form.cleaned_data['community_certificate'],
                community_certificate_no = comm_certificate_no,
                community_certificate_date = comm_certificate_date,
                nativity_certificate = form.cleaned_data['nativity_certificate'],
                religion = form.cleaned_data['religion'],
                mothertounge = form.cleaned_data['mothertounge'],
                phone_number = form.cleaned_data['phone_number'],
                email = form.cleaned_data['email'],
                child_differently_abled = form.cleaned_data['child_differently_abled'],
                differently_abled = form.cleaned_data['differently_abled'],
                child_admitted_under_reservation = form.cleaned_data['child_admitted_under_reservation'],
                weaker_section = form.cleaned_data['weaker_section'],
                weaker_section_income_certificate_no = form.cleaned_data['weaker_section_income_certificate_no'],
                child_disadvantaged_group = form.cleaned_data['child_disadvantaged_group'],
                disadvantaged_group = form.cleaned_data['disadvantaged_group'],
                subcaste = form.cleaned_data['subcaste'],
                nationality = form.cleaned_data['nationality'],
                house_address = form.cleaned_data['house_address1'],
                street_name = form.cleaned_data['house_address2'],
                area_village = form.cleaned_data['house_address3'],
                city_district = form.cleaned_data['house_address4'],
                native_district = form.cleaned_data['native_district'],
                pin_code = form.cleaned_data['pin_code'],
                blood_group = form.cleaned_data['blood_group'],
                mother_name = form.cleaned_data['mother_name'],
                mother_occupation = form.cleaned_data['mother_occupation'],
                father_name = form.cleaned_data['father_name'],
                father_occupation = form.cleaned_data['father_occupation'],
                parent_income = form.cleaned_data['parent_income'],
                guardian_name = form.cleaned_data['guardian_name'],
                class_studying = form.cleaned_data['class_studying'],
                class_section = form.cleaned_data['class_section'],
                group_code = form.cleaned_data['group_code'],
                sport_participation = form.cleaned_data['sport_participation'],
                education_medium = form.cleaned_data['education_medium'],
                state = form.cleaned_data['state'],
                district = form.cleaned_data['district'],
                block = form.cleaned_data['block'],
                unique_id_no = form.cleaned_data['unique_id_no'],
                school = form.cleaned_data['school'],
                staff_id = form.cleaned_data['staff_id'],
                student_admitted_section = form.cleaned_data['student_admitted_section'],
                school_admission_no = form.cleaned_data['school_admission_no'],
                bank = form.cleaned_data['bank'],
                bank_branch = form.cleaned_data['bank_branch'],
                bank_account_no = form.cleaned_data['bank_account_no'],
                bank_ifsc_code = form.cleaned_data['bank_ifsc_code'],
                sports_player = form.cleaned_data['sports_player'],
                sports_name = form.cleaned_data['sports_name'],
                # govt_schemes_status = form.cleaned_data['govt_schemes_status'],
                schemes = scheme_lst,
                academic_year = form.cleaned_data['academic_year'],
                height = form.cleaned_data['height'],
                weight = form.cleaned_data['weight'],
                laptop_issued = form.cleaned_data['laptop_issued'],
                laptop_slno = form.cleaned_data['laptop_slno'],
                nutritious_meal_flag = nutritious_meal_flag,
                scholarship_from_other_source = form.cleaned_data['scholarship_from_other_source'],
                scholarship_details = form.cleaned_data['scholarship_details'],
                scholarship_other_details = form.cleaned_data['scholarship_other_details'],
                bus_pass = form.cleaned_data['bus_pass'],
                bus_from_route = form.cleaned_data['bus_from_route'],
                bus_to_route = form.cleaned_data['bus_to_route'],
                bus_route_no = form.cleaned_data['bus_route_no'],
                )
            child.save()
            

            child_new_id = Child_detail.objects.get(unique_id_no=child.unique_id_no)
            if child_new_id.community_certificate == "No":
                child_new_id.community_certificate_date = None
                child_new_id.save()
            else:
                pass

            try:
                fmdetail_no = request.POST.getlist('fmdetail_no')
                fmdetail_name = request.POST.getlist('sibling_name')
                fmdetail_rel = request.POST.getlist('sibling_relationship')
                fmdetail_age = request.POST.getlist('sibling_age')
                fmdetail_studying = request.POST.getlist('sibling_studying')
                fmdetail_status = request.POST.getlist('sibling_status')
                fmdetail_school = request.POST.getlist('sibling_studying_same_school')
                for entry in range(len(fmdetail_no)):
                    newchild_fmdetail = Child_family_detail(
                        child_key = child_new_id,
                        si_no  = fmdetail_no[entry],
                        block = child.block,
                        sibling_name = fmdetail_name[entry],
                        sibling_relationship = fmdetail_rel[entry],
                        sibling_age = fmdetail_age[entry],
                        sibling_studying = fmdetail_studying[entry],
                        sibling_status = fmdetail_status[entry],
                        sibling_studying_same_school = fmdetail_school[entry],
                        staff_id = child.staff_id,
                    )
                    newchild_fmdetail.save()
            except Exception:
                pass
            msg = "Child    " + form.cleaned_data['name'] + "  added successfully"
            messages.success(request, msg )
            return HttpResponseRedirect(reverse('students_child_detail_list'))
        else:
            district_list = District.objects.all().exclude(district_name='None').order_by('district_name')
            differently_abled_list = Differently_abled.objects.all().order_by('da_name')
            dis_advantaged_list = Disadvantaged_group.objects.all().order_by('dis_group_name')
            schemes = Schemes.objects.all().order_by('scheme_name')
            return render (request,'students/child_detail/child_detail_form.html',{'form':form,'district_list':district_list,'schemes':schemes,'differently_abled_list':differently_abled_list,'dis_advantaged_list':dis_advantaged_list})


    
class Child_detailDateDetailView(Child_detailDateView, DateDetailView):

    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailDayArchiveView(
        Child_detailDateView, Child_detailBaseListView, DayArchiveView):

    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailDeleteView(Child_detailView, DeleteView):
    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailDetailView(View):
    @method_decorator(login_required)
    def get (self,request,**kwargs):
        pk=self.kwargs.get('pk')
        childdetail = Child_detail.objects.get(id=pk)
        differently_abled_list1=childdetail.differently_abled
        disadvantaged_group_list1=childdetail.disadvantaged_group
        scheme_lst1=childdetail.schemes
        fmdetail = Child_family_detail.objects.filter(child_key=pk)
        if childdetail.nutritious_meal_flag == '1':
            nutritious_meal_programme = "Yes"
        else:
            nutritious_meal_programme = "No"
        return render(request,'students/child_detail/object_table_detail.html',{'fmdetail':fmdetail,'object':childdetail,'schemes':scheme_lst1,'differently_abled_list':differently_abled_list1,'disadvantaged_group_list':disadvantaged_group_list1,'nutritious_meal_programme':nutritious_meal_programme})

class Child_detailClasswiseView(View):
    
    @method_decorator(login_required)
    def get(self,request,**kwargs):
        class_id = self.kwargs.get('cl_id')
        school_code = self.kwargs.get('school_code')
        school_id = request.user.account.associated_with
        schl_id = School.objects.get(id=school_id)
        child_detail_main_list = Child_detail.objects.filter(district_id = schl_id.district_id , block_id = schl_id.block_id)
        # if request.user.account.user_category_id == 2:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 5:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, district_id= request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
        #     child_detail_list = child_detail_main_list.filter(staff_id=school_code).exclude(transfer_flag = 1)    
        # else:
        #     child_detail_list = child_detail_main_list.filter(staff_id=schl_id.school_code).exclude(transfer_flag = 1)
        if request.user.account.user_category_id == 2:
            child_detail_list = Child_detail.objects.filter(school_id=schl_id.id, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        elif request.user.account.user_category_id == 5:
            child_detail_list = Child_detail.objects.filter(school_id=schl_id.id, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
            child_detail_list = Child_detail.objects.filter(school_id=schl_id.id, district_id= request.user.account.associated_with).exclude(transfer_flag = 1)
        elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
            child_detail_list = child_detail_main_list.filter(school_id=schl_id.id).exclude(transfer_flag = 1)    
        else:
            child_detail_list = child_detail_main_list.filter(school_id=schl_id.id).exclude(transfer_flag = 1)
        classwise_detail = child_detail_list.filter(class_studying_id=class_id).order_by('name')
        classwise_detail_count = classwise_detail.count()
        paginator = Paginator(classwise_detail, 10)
        page = request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'students/child_detail/child_detail_classwise_list.html',{'page_objs':page_obj,'classwise_detail':classwise_detail,'school_code':school_code,'class_id':class_id,'classwise_detail_count':classwise_detail_count})

class Child_detailClasswiseListView(View):
    
    @method_decorator(login_required)
    def get(self,request,**kwargs):
        class_id = self.kwargs.get('cl_id')
        school_code = self.kwargs.get('school_code')
        schl_id = School.objects.get(school_code=school_code)

        # if request.user.account.user_category_id == 2:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 5:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, district_id= request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code).exclude(transfer_flag = 1)    
        # else:
        #     child_detail_list = Child_detail.objects.filter(staff_id=schl_id.school_code).exclude(transfer_flag = 1)
        if request.user.account.user_category_id == 2:
            child_detail_list = Child_detail.objects.filter(school__id=schl_id.id, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        elif request.user.account.user_category_id == 5:
            child_detail_list = Child_detail.objects.filter(school__id=schl_id.id, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
            child_detail_list = Child_detail.objects.filter(school__id=schl_id.id, district_id= request.user.account.associated_with).exclude(transfer_flag = 1)
        elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
            child_detail_list = Child_detail.objects.filter(school__id=schl_id.id).exclude(transfer_flag = 1)    
        else:
            child_detail_list = Child_detail.objects.filter(school_id=schl_id.id).exclude(transfer_flag = 1)
        classwise_detail = child_detail_list.filter(class_studying_id=class_id).order_by('name')
        classwise_detail_count = classwise_detail.count()
        paginator = Paginator(classwise_detail, 10)
        page = request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'students/child_detail/child_detail_classwise_list.html',{'page_objs':page_obj,'classwise_detail':classwise_detail,'school_code':school_code,'class_id':class_id,'classwise_detail_count':classwise_detail_count})



class Child_detailListView(View):

    @method_decorator(login_required)
    def get(self,request,**kwargs):
        try:
            school_code = self.request.GET.get('school_code')
            if request.user.account.user_category_id == 1:
                pass
            else:
                school_details = School.objects.get(school_code=school_code)
                schl_id = school_details.id
            if request.user.account.user_category_id == 2:
                child_detail_list = School_child_count.objects.get(school_id=schl_id, school__block_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 3:
                child_detail_list = School_child_count.objects.get(school_id=schl_id, school__district_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 5:
                child_detail_list = School_child_count.objects.get(school_id=schl_id, school__block_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
                child_detail_list = School_child_count.objects.get(school_id=schl_id, school__district_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
                child_detail_list = School_child_count.objects.get(school_id=schl_id)    
            else:
                child_detail_list = School_child_count.objects.get(school_id=request.user.account.associated_with)

            totalcount = child_detail_list.total_count
            I = child_detail_list.one
            II = child_detail_list.two
            III = child_detail_list.three
            IV = child_detail_list.four
            V = child_detail_list.five
            VI = child_detail_list.six
            VII = child_detail_list.seven
            VIII = child_detail_list.eight
            IX = child_detail_list.nine
            X = child_detail_list.ten
            XI = child_detail_list.eleven
            XII = child_detail_list.twelve
            return render(request,'students/child_detail/object_table_list.html',{'child_detail_list':child_detail_list,'totalcount':totalcount,'I':I,'II':II,'III':III,'IV':IV,'V':V,'VI':VI,'VII':VII,'VIII':VIII,'IX':IX,'X':X,'XI':XI,'XII':XII,'school_code':school_code})
        except School_child_count.DoesNotExist:
            messages.add_message(
                self.request,
                messages.ERROR,"No School."
            )
            return render(request,'students/child_detail/object_table_list.html')
        
    @method_decorator(login_required)
    def post(self,request,**kwargs):
        if request.POST['search_id']!='':
            if str(request.user.account.user_category) == 'block':
                child_search = Child_detail.objects.filter(Q(block_id=request.user.account.associated_with,unique_id_no__icontains=request.POST['search_id']) | Q(block_id=request.user.account.associated_with,name__icontains=request.POST['search_id']))
            elif str(request.user.account.user_category) == 'district':
                child_search = Child_detail.objects.filter(Q(district_id=request.user.account.associated_with,unique_id_no__icontains=request.POST['search_id']) | Q(district_id=request.user.account.associated_with,name__icontains=request.POST['search_id']))
            elif str(request.user.account.user_category) == 'state':
                child_search = Child_detail.objects.filter(Q(unique_id_no__icontains=request.POST['search_id']) | Q(name__icontains=request.POST['search_id']))
            else:
                child_search = Child_detail.objects.filter(Q(staff_id=request.user,unique_id_no__icontains=request.POST['search_id']) | Q(staff_id=request.user,name__icontains=request.POST['search_id']))
            return render(request,'students/child_detail/child_detail_classwise_list.html',{'child_search':child_search})


class Child_detailMonthArchiveView(
        Child_detailDateView, Child_detailBaseListView, MonthArchiveView):

    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailTodayArchiveView(
        Child_detailDateView, Child_detailBaseListView, TodayArchiveView):

    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailUpdateView(View):
    @method_decorator(login_required)
    def get(self, request,**kwargs): 
        pk=self.kwargs.get('pk')
        instance = Child_detail.objects.get(id=pk)
        differently_abled_list1 = instance.differently_abled
        disadvantaged_group1 = instance.disadvantaged_group
        schemes1 =instance.schemes
        sport_participation = instance.sport_participation
        sports_name = instance.sports_name
        if instance.nutritious_meal_flag == '1':
            nutritious_meal_programme = "Yes"
        else:
            nutritious_meal_programme = "No"
        try:
            fmdetail = Child_family_detail.objects.filter(child_key=pk)

        except Exception:
            fmdetail =None
        district_list = District.objects.all().exclude(district_name='None').order_by('district_name')
        form = Child_detailform(instance=instance)
        ge = instance.gender
        grp= instance.group_code
        cls_studying = instance.class_studying
        cls_section = instance.class_section
        academic_yr = instance.academic_year
        mother_ocu = instance.mother_occupation
        father_ocu = instance.father_occupation
        bg = instance.blood_group
        st_status = instance.child_status
        mothrtongue = instance.mothertounge
        edu_medium = instance.education_medium
        nationality_value = instance.nationality
        religion_value = instance.religion
        stud_admitted_section = instance.student_admitted_section
        bank_name = instance.bank
        attndce_status = instance.attendance_status
        scholarship_dtls = instance.scholarship_details
        diffntly_abled = instance.differently_abled
        dis_advntgd_grp = instance.disadvantaged_group
        differently_abled_list = Differently_abled.objects.all()
        dis_advantaged_list = Disadvantaged_group.objects.all()
        language_list = Language.objects.all().exclude(language_name='Undefined').order_by('language_name')
        education_medium_list = Education_medium.objects.all().exclude(education_medium='Undefined').order_by('education_medium')
        religion_list = Religion.objects.all().exclude(religion_name='Undefined').order_by('id')
        community_list = Community.objects.all().exclude(community_name='undefined').order_by('id')
        
        nationality_list = Nationality.objects.all().exclude(nationality='Undefined').order_by('id')
        schemes = Schemes.objects.all()
        mthr_name = instance.mother_name
        class_studying_list = Class_Studying.objects.all()[:12]
        group_code_list = Group_code.objects.all()
        bank_list = Bank.objects.all()
        state_list = State.objects.all().order_by('state_name')
        photo = instance.photograph
        try:
            parent_income_list = Parent_annual_income.objects.all().order_by('id')
            parent_income = Parent_annual_income.objects.get(id=instance.parent_income)
        except Parent_annual_income.DoesNotExist:

            parent_income = 0
        govt_aid_school_management_list = [1,2,3,4,5,6,7]
        aid_school_management_list = [6,7]
        private_school_management_list = [8,9,10,11,12,13,14,15,16,17,18]
        onetoten = [1,2,3,4,5,6,7,8,9,10]
        onetotwelve = [1,2,3,4,5,6,7,8,9,10,11,12]
        onetoeight = [1,2,3,4,5,6,7,8]
        return render(request, 'students/child_detail/child_detail_form.html', {'grp':grp,'form': form,'fmdetail':fmdetail,'district_list':district_list,'pk1':pk,'schemes':schemes,'differently_abled_list':differently_abled_list,'dis_advantaged_list':dis_advantaged_list,'ge':ge,'cls_section':cls_section,'cls_studying':cls_studying,'academic_yr':academic_yr,'mother_ocu':mother_ocu,'father_ocu':father_ocu,'bg':bg,'st_status':st_status,'differently_abled_list1':differently_abled_list1,'disadvantaged_group1':disadvantaged_group1,'schemes1':schemes1,'sport_participation':sport_participation,'sports_name':sports_name,'mthr_name':mthr_name,'nutritious_meal_programme':nutritious_meal_programme,'state_list':state_list,'parent_income_list':parent_income_list,'parent_income':parent_income,'class_studying_list':class_studying_list,'group_code_list':group_code_list,'bank_list':bank_list,'education_medium_list':education_medium_list,'nationality_list':nationality_list,'religion_list':religion_list,'community_list':community_list,'language_list':language_list,'mothrtongue':mothrtongue,'edu_medium':edu_medium,'nationality_value':nationality_value,'religion_value':religion_value,'parent_income':parent_income,'govt_aid_school_management_list':govt_aid_school_management_list,'aid_school_management_list':aid_school_management_list,'private_school_management_list':private_school_management_list,'onetoten':onetoten,'stud_admitted_section':stud_admitted_section,'onetotwelve':onetotwelve,'onetoeight':onetoeight,'bank_name':bank_name,'scholarship_dtls':scholarship_dtls,'attndce_status':attndce_status,'diffntly_abled':diffntly_abled,'photo':photo,'dis_advntgd_grp':dis_advntgd_grp})

    @method_decorator(login_required)
    def post(self,request,**kwargs):
        pk=self.kwargs.get('pk')
        instance = Child_detail.objects.get(id=pk)
        cls_studying = instance.class_studying
        cls_section = instance.class_section
        academic_yr = instance.academic_year
        stud_photo = instance.photograph
        bank_name = instance.bank
        differently_abled_list1 = instance.differently_abled
        student_count = School_child_count.objects.get(school_id = instance.school_id)
        form = Child_detailform(request.POST,request.FILES)
        if form.is_valid():
            child_edit = Child_detail.objects.get(id=pk)
            class_studying_detail = child_edit.class_studying

            # if form.cleaned_data["child_differently_abled"]  == "Yes":
            #     if differently_abled_list1 != form.cleaned_data["differently_abled"]:
            #         diff_abled = form.cleaned_data["differently_abled"]
            #     else:
            #         diff_abled = differently_abled_list1
            # else:
            #     diff_abled = form.cleaned_data['differently_abled']

            # if form.cleaned_data["child_disadvantaged_group"] == 'Yes':
            #     dis_group_lst=''
            #     if request.POST.getlist("disadvantaged_group1"):

            #         disadvantaged_group1 = request.POST.getlist("disadvantaged_group1")
            #         for group3 in disadvantaged_group1:
            #             dis_group_lst = dis_group_lst + group3
            #     if form.cleaned_data["disadvantaged_group"]:
            #         dis_group_list=request.POST.getlist('disadvantaged_group')
                    
            #         for group in dis_group_list:
            #             dis_group_lst=dis_group_lst+group+','
            # else:
            #     dis_group_lst = "N/A"
            # if form.cleaned_data['govt_schemes_status'] == "Yes":
                
            #     if request.POST.getlist("schemes1"):
            #         scheme_lst = ''
            #         schemes1 = request.POST.getlist("schemes1")
            #         for group4 in schemes1:
            #             scheme_lst = scheme_lst + group4
            #     if form.cleaned_data['schemes']:
            #         scheme_list=request.POST.getlist('schemes')
                    
            #         for scheme in scheme_list:
            #             scheme_lst=scheme_lst+scheme+','
            # else:
            #     scheme_lst = "N/A"
            # if stud_photo:
            #     student_photo = stud_photo
            # else:
            #     student_photo = form.cleaned_data['photograph']


            # if request.POST.get('clear_photo', True):
            #     clear_photo = 'yes'
            # elif request.POST.get('clear_photo', False):
            #     clear_photo = 'No'
            # else:
            #     pass

            if form.cleaned_data["child_differently_abled"]  == "Yes":
                diff_abled = form.cleaned_data["differently_abled"]
            else:
                diff_abled = ''

            if form.cleaned_data["weaker_section"]  == "Yes":
                weaker_sec_incm_certi_no = form.cleaned_data["weaker_section_income_certificate_no"]
            else:
                weaker_sec_incm_certi_no = ''

            if form.cleaned_data["child_disadvantaged_group"]  == "Yes":
                dis_advntgd_grp = form.cleaned_data["disadvantaged_group"]
            else:
                dis_advntgd_grp = ''

            
            
            if stud_photo == '':
                student_photo = form.cleaned_data['photograph']
            else:
                if request.POST.get('clear_photo') == "True":
                    student_photo = form.cleaned_data['photograph']
                else:
                    student_photo = stud_photo        

            if form.cleaned_data['schemes']:
                scheme_list=request.POST.getlist('schemes')
                scheme_lst=''
                for scheme in scheme_list:
                    scheme_lst=scheme_lst+scheme+','
            else:
                scheme_lst = form.cleaned_data['schemes']
            
            # if form.cleaned_data['house_address']:
            #     address_detail = request.POST.getlist('house_address')
            #     address=''
            #     for adrs in address_detail:
            #         address=address+adrs+','
            # else:
            #     address = form.cleaned_data['house_address']

            if form.cleaned_data['nutritious_meal_flag'] == "Yes":
                nutritious_meal_flag = 1
            else:
                nutritious_meal_flag = 0

            if form.cleaned_data['aadhaar_id'] == "Yes":
                aadhaar_uid_num = form.cleaned_data['aadhaar_uid_number']
            else:
                aadhaar_uid_num = int()

            if form.cleaned_data['community_certificate'] == "Yes":
                comm_certificate_no = form.cleaned_data['community_certificate_no']
                comm_certificate_date = form.cleaned_data['community_certificate_date']
            else:
                comm_certificate_no = ''
                comm_certificate_date = '1111-11-11'

            if form.cleaned_data['bus_pass'] == "Yes":
            	bs_from_route = form.cleaned_data['bus_from_route']
            	bs_to_route = form.cleaned_data['bus_to_route']
            	bs_route_no = form.cleaned_data['bus_route_no']
            else:
            	bs_from_route = ''
            	bs_to_route = ''
            	bs_route_no = ''

            if form.cleaned_data['scholarship_from_other_source'] == "Yes":
                schlrshp_details = form.cleaned_data['scholarship_details']                
                schlrshp_othr_details = form.cleaned_data['scholarship_other_details']
            else:
                schlrshp_details = ''
                schlrshp_othr_details = ''
            
            if form.cleaned_data['sports_player'] == "Yes":
                sprt_participation = form.cleaned_data['sport_participation']                
                sprts_name = form.cleaned_data['sports_name']
            else:
                sprt_participation = ''
                sprts_name = ''

            child_edit.name = form.cleaned_data['name']
            child_edit.name_tamil = form.cleaned_data['name_tamil']
            child_edit.aadhaar_id = form.cleaned_data['aadhaar_id']
            child_edit.aadhaar_uid_number = aadhaar_uid_num
            child_edit.photograph = student_photo
            child_edit.photo = student_photo
            child_edit.gender = form.cleaned_data['gender']
            child_edit.dob = form.cleaned_data['dob']
            child_edit.community = form.cleaned_data['community']
            child_edit.community_certificate = form.cleaned_data['community_certificate']
            child_edit.community_certificate_no = comm_certificate_no
            child_edit.community_certificate_date = comm_certificate_date
            child_edit.nativity_certificate = form.cleaned_data['nativity_certificate']
            child_edit.religion = form.cleaned_data['religion']
            child_edit.mothertounge = form.cleaned_data['mothertounge']
            child_edit.phone_number = form.cleaned_data['phone_number']
            child_edit.email = form.cleaned_data['email']
            child_edit.child_differently_abled = form.cleaned_data['child_differently_abled']
            child_edit.differently_abled = diff_abled
            child_edit.child_admitted_under_reservation = form.cleaned_data['child_admitted_under_reservation']
            child_edit.weaker_section = form.cleaned_data['weaker_section']
            child_edit.weaker_section_income_certificate_no = weaker_sec_incm_certi_no
            child_edit.child_disadvantaged_group = form.cleaned_data['child_disadvantaged_group']
            child_edit.disadvantaged_group = dis_advntgd_grp
            child_edit.subcaste = form.cleaned_data['subcaste']
            child_edit.nationality = form.cleaned_data['nationality']
            child_edit.child_status = form.cleaned_data['child_status']
            child_edit.house_address = form.cleaned_data['house_address']
            child_edit.street_name = form.cleaned_data['street_name']
            child_edit.area_village = form.cleaned_data['area_village']
            child_edit.city_district = form.cleaned_data['city_district']
            child_edit.native_district = form.cleaned_data['native_district']
            child_edit.pin_code = form.cleaned_data['pin_code']
            child_edit.blood_group = form.cleaned_data['blood_group']
            child_edit.guardian_name = form.cleaned_data['guardian_name']
            child_edit.mother_name = form.cleaned_data['mother_name']
            child_edit.mother_occupation = form.cleaned_data['mother_occupation']
            child_edit.father_name = form.cleaned_data['father_name']
            child_edit.father_occupation = form.cleaned_data['father_occupation']
            child_edit.parent_income = form.cleaned_data['parent_income']
            child_edit.class_studying = form.cleaned_data['class_studying']
            child_edit.class_section = form.cleaned_data['class_section']
            child_edit.group_code = form.cleaned_data['group_code']
            child_edit.attendance_status = form.cleaned_data['attendance_status']
            child_edit.sport_participation = sprt_participation
            child_edit.sports_player = form.cleaned_data['sports_player']
            child_edit.sports_name = sprts_name
            child_edit.education_medium = form.cleaned_data['education_medium']
            child_edit.state = form.cleaned_data['state']
            child_edit.district = form.cleaned_data['district']
            child_edit.block = form.cleaned_data['block']
            child_edit.school = form.cleaned_data['school']
            child_edit.student_admitted_section = form.cleaned_data['student_admitted_section']
            child_edit.school_admission_no = form.cleaned_data['school_admission_no']
            child_edit.staff_id = form.cleaned_data['staff_id']
            if form.cleaned_data['bank']:
                child_edit.bank = form.cleaned_data['bank']
            if form.cleaned_data['bank_branch']:
                child_edit.bank_branch = form.cleaned_data['bank_branch']
            if form.cleaned_data['bank_account_no']:
                child_edit.bank_account_no = form.cleaned_data['bank_account_no']
            if form.cleaned_data['bank_ifsc_code']:
                child_edit.bank_ifsc_code = form.cleaned_data['bank_ifsc_code']
            # child_edit.govt_schemes_status = form.cleaned_data['govt_schemes_status']
            child_edit.schemes = scheme_lst
            child_edit.academic_year = form.cleaned_data['academic_year']
            child_edit.height = form.cleaned_data['height']
            child_edit.weight = form.cleaned_data['weight']
            if form.cleaned_data['laptop_issued']:
                child_edit.laptop_issued = form.cleaned_data['laptop_issued']
            if form.cleaned_data['laptop_slno']:
                child_edit.laptop_slno = form.cleaned_data['laptop_slno']
            child_edit.nutritious_meal_flag = nutritious_meal_flag
            child_edit.bus_pass = form.cleaned_data['bus_pass']
            child_edit.bus_from_route = bs_from_route
            child_edit.bus_to_route = bs_to_route
            child_edit.bus_route_no = bs_route_no
            child_edit.scholarship_from_other_source = form.cleaned_data['scholarship_from_other_source']
            child_edit.scholarship_details = schlrshp_details
            child_edit.scholarship_other_details = schlrshp_othr_details
            child_edit.save()
            if child_edit.community_certificate == "No":
                child_edit.community_certificate_date = None
                child_edit.save()
            else:
                pass

            
            if cls_studying != child_edit.class_studying:
                clss_studying = Class_Studying.objects.get(class_studying = child_edit.class_studying)
                if str(cls_studying)=='I':
                    student_count.one -= 1
                elif str(cls_studying)=='II':
                    student_count.two -= 1
                elif str(cls_studying)=='III':
                    student_count.three -= 1
                elif str(cls_studying)=='IV':
                    student_count.four -= 1
                elif str(cls_studying)=='V':
                    student_count.five -= 1
                elif str(cls_studying)=='VI':
                    student_count.six -= 1
                elif str(cls_studying)=='VII':
                    student_count.seven -= 1
                elif str(cls_studying)=='VIII':
                    student_count.eight -= 1
                elif str(cls_studying)=='IX':
                    student_count.nine-= 1
                elif str(cls_studying)=='X':
                    student_count.ten -= 1
                elif str(cls_studying)=='XI':
                    student_count.eleven -= 1
                elif str(cls_studying)=='XII':
                    student_count.twelve -= 1
                student_count.total_count -= 1

                if str(clss_studying)=='I':
                    student_count.one += 1
                elif str(clss_studying)=='II':
                    student_count.two += 1
                elif str(clss_studying)=='III':
                    student_count.three += 1
                elif str(clss_studying)=='IV':
                    student_count.four += 1
                elif str(clss_studying)=='V':
                    student_count.five += 1
                elif str(clss_studying)=='VI':
                    student_count.six += 1
                elif str(clss_studying)=='VII':
                    student_count.seven += 1
                elif str(clss_studying)=='VIII':
                    student_count.eight += 1
                elif str(clss_studying)=='IX':
                    student_count.nine+= 1
                elif str(clss_studying)=='X':
                    student_count.ten += 1
                elif str(clss_studying)=='XI':
                    student_count.eleven += 1
                elif str(clss_studying)=='XII':
                    student_count.twelve += 1
                student_count.total_count += 1
                student_count.save()
            else:
                pass


            try:
   
                fmdetail_no = request.POST.getlist('fmdetail_no')
                fmdetail_name = request.POST.getlist('sibling_name')
                fmdetail_rel = request.POST.getlist('sibling_relationship')
                fmdetail_age = request.POST.getlist('sibling_age')
                fmdetail_studying = request.POST.getlist('sibling_studying')
                fmdetail_status = request.POST.getlist('sibling_status')
                fmdetail_school = request.POST.getlist('sibling_studying_same_school')
                fmdetail_count = Child_family_detail.objects.filter(child_key=pk).count()
                fmdetail_existing = Child_family_detail.objects.filter(child_key=pk)
                si_no_in_db = list()
                
                if (len(fmdetail_no)) > fmdetail_count:
                    for p in fmdetail_existing:
                        si_no_in_db.append(p.si_no)
                    final_si_no1 = list(set(fmdetail_no)-set(si_no_in_db))
                    final_si_no =  final_si_no1[-1]
                    # final_si_no = list(set(fmdetail_no)-set(si_no_in_db))
                    # if len(final_si_no1) > 1:

                    # else:
                    for entry in range(len(final_si_no)):
                        newchild_fmdetail = Child_family_detail(
                            child_key = child_edit,
                            si_no  = fmdetail_no[entry],
                            block = child_edit.block,
                            sibling_name = fmdetail_name[entry],
                            sibling_relationship = fmdetail_rel[entry],
                            sibling_age = fmdetail_age[entry],
                            sibling_studying = fmdetail_studying[entry],
                            sibling_status = fmdetail_status[entry],
                            sibling_studying_same_school = fmdetail_school[entry],
                            staff_id = child_edit.staff_id,
                        )
                        newchild_fmdetail.save()


                for entry in range(len(fmdetail_no)): 
                    newchild_fmdetail_edit = Child_family_detail.objects.get(child_key=pk,si_no=fmdetail_no[entry])
                    newchild_fmdetail_edit.child_key = child_edit
                    newchild_fmdetail_edit.si_no  = fmdetail_no[entry]
                    newchild_fmdetail_edit.block = child_edit.block
                    newchild_fmdetail_edit.sibling_name = fmdetail_name[entry]
                    newchild_fmdetail_edit.sibling_relationship = fmdetail_rel[entry]
                    newchild_fmdetail_edit.sibling_age = fmdetail_age[entry]
                    newchild_fmdetail_edit.sibling_studying = fmdetail_studying[entry]
                    newchild_fmdetail_edit.sibling_status = fmdetail_status[entry]
                    newchild_fmdetail_edit.sibling_studying_same_school = fmdetail_school[entry]
                    newchild_fmdetail_edit.staff_id = child_edit.staff_id
                    newchild_fmdetail_edit.save()
            except Child_family_detail.DoesNotExist:
                pass

            
        else:
            return render (request,'students/child_detail/child_detail_form.html',{'form':form,'pk1':pk,'cls_studying':cls_studying,'academic_yr':academic_yr,'bank_name':bank_name,'diff_abled':diff_abled})
        msg = "Child    " + form.cleaned_data['name'] + "  updated successfully"
        messages.success(request, msg )
        return HttpResponseRedirect(reverse('students_child_detail_list'))

    


class Child_detailWeekArchiveView(
        Child_detailDateView, Child_detailBaseListView, WeekArchiveView):

    @method_decorator(login_required)
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_detail_list')


class Child_detailYearArchiveView(
        Child_detailDateView, Child_detailBaseListView, YearArchiveView):
    make_object_list = True





class Child_detailTransferView(View):
    @method_decorator(login_required)
    def get(self,request,**kwargs):
        pk=self.kwargs.get('pk')
        instance = Child_detail.objects.get(id=pk)
        form = Child_detailform(instance=instance)
        return render(request,'students/child_detail/child_detail_transfer.html',{'form':form,'pk1':pk})
    @method_decorator(login_required)    
    def post(self,request,**kwargs):
        pk=self.kwargs.get('pk')
        child_edit = Child_detail.objects.get(id=pk)

        form = Child_detailform()

            
        if request.POST['transfer_date']:
            child_edit.transfer_flag = 1
            child_edit.transfer_date = datetime.strptime(request.POST['transfer_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
            child_edit.save()
            child_dtl = Child_detail.objects.get(id=pk)
            if child_dtl.transfer_flag == 1:
                school_count = School_child_count.objects.get(school_id=request.user.account.associated_with)
                if child_dtl.class_studying_id == 1:
                    school_count.one = school_count.one-1
                elif child_dtl.class_studying_id == 2:
                    school_count.two = school_count.two-1
                elif child_dtl.class_studying_id == 3:
                    school_count.three = school_count.three-1
                elif child_dtl.class_studying_id == 4:
                    school_count.four = school_count.four-1
                elif child_dtl.class_studying_id == 5:
                    school_count.five = school_count.five-1
                elif child_dtl.class_studying_id == 6:
                    school_count.six = school_count.six-1
                elif child_dtl.class_studying_id == 7:
                    school_count.seven = school_count.seven-1
                elif child_dtl.class_studying_id == 8:
                    school_count.eight = school_count.eight-1
                elif child_dtl.class_studying_id == 9:
                    school_count.nine = school_count.nine-1
                elif child_dtl.class_studying_id == 10:
                    school_count.ten = school_count.ten-1
                elif child_dtl.class_studying_id == 11:
                    school_count.eleven = school_count.eleven-1
                elif child_dtl.class_studying_id == 12:
                    school_count.twelve = school_count.twelve-1
                school_count.save()

        else:
            # return render (request,'students/child_detail/child_detail_transfer.html',{'form':form,'pk1':pk})
            return HttpResponseRedirect(reverse('students_child_detail_list'))

        return HttpResponseRedirect(reverse('students_child_detail_list'))




class Child_detailPoolView(View):

    @method_decorator(login_required)
    def get(self,request,**kwargs):
        form = Pool_databaseform
        return render(request,'students/child_detail/child_detail_pool_detail.html',{'form':form})
        
    @method_decorator(login_required)
    def post(self,request,**kwargs):
        dist_id = self.request.POST.get('district')
        blk_id = self.request.POST.get('block')
        schl_id = self.request.POST.get('school')
        class_last_studied = self.request.POST.get('class_last_studied')
        student_list = Child_detail.objects.filter(school_id = schl_id, class_studying = class_last_studied, transfer_flag= 1)

        return render(request,'students/child_detail/child_detail_pool_detail.html',{'student_list':student_list})

class Child_detailPoolUpdateView(View):
    @method_decorator(login_required)
    def get(self,request,**kwargs):
        form = Pool_databaseform
        unique_id_no = self.kwargs.get('pk')
        chld_detail = Child_detail.objects.get(unique_id_no=unique_id_no)
        dist_id = chld_detail.district_id
        blk_id = chld_detail.block_id
        schl_id = chld_detail.school_id
        class_studying = chld_detail.class_studying_id
        class_studying_list = [1,2,3,4,5,6,7,8,9,10,11,12]
        return render(request,'students/child_detail/child_detail_pool_update.html',{'form':form,'unique_id_no':unique_id_no,'dist_id':dist_id,'blk_id':blk_id,'schl_id':schl_id,'class_studying':class_studying,'class_studying_list':class_studying_list})
    @method_decorator(login_required)
    def post(self,request,**kwargs):
        unique_id_no = self.kwargs.get('pk')
        chld_detail = Child_detail.objects.get(unique_id_no=unique_id_no)
        dist_id = chld_detail.district
        blk_id = chld_detail.block
        schl_id = chld_detail.school
        class_last_studied = chld_detail.class_studying
        migrated_school = request.user.account.associated_with
        migrated_schl = School.objects.get(id=migrated_school)
        form = Pool_databaseform(request.POST)
        if form.is_valid():
            pool_detail = Child_detail_pool_database(
                district = dist_id,
                block = blk_id,
                school = schl_id,
                class_last_studied = class_last_studied,
                unique_id_no = unique_id_no,
                class_studying = form.cleaned_data['class_studying'],
                migrated_school = migrated_school,
                )
            pool_detail.save()
            chld_detail.district = migrated_schl.district
            chld_detail.block = migrated_schl.block
            chld_detail.school = migrated_schl
            chld_detail.staff_id = migrated_schl.school_code
            chld_detail.class_studying = form.cleaned_data['class_studying']
            chld_detail.transfer_flag = 2
            chld_detail.save()
            if chld_detail.transfer_flag == 2:
                schl_detail = School_child_count.objects.get(school_id=chld_detail.school)
                if chld_detail.class_studying_id == 1:
                    schl_detail.one = schl_detail.one+1
                elif chld_detail.class_studying_id == 2:
                    schl_detail.two = schl_detail.two+1
                elif chld_detail.class_studying_id == 3:
                    schl_detail.three = schl_detail.three+1
                elif chld_detail.class_studying_id == 4:
                    schl_detail.four = schl_detail.four+1
                elif chld_detail.class_studying_id == 5:
                    schl_detail.five = schl_detail.five+1
                elif chld_detail.class_studying_id == 6:
                    schl_detail.six = schl_detail.six+1
                elif chld_detail.class_studying_id == 7:
                    schl_detail.seven = schl_detail.seven+1
                elif chld_detail.class_studying_id == 8:
                    schl_detail.eight = schl_detail.eight+1
                elif chld_detail.class_studying_id == 9:
                    schl_detail.nine = schl_detail.nine+1
                elif chld_detail.class_studying_id == 10:
                    schl_detail.ten = schl_detail.ten+1
                elif chld_detail.class_studying_id == 11:
                    schl_detail.eleven = schl_detail.eleven+1
                elif chld_detail.class_studying_id == 12:
                    schl_detail.twelve = schl_detail.twelve+1
                schl_detail.save()
        return render(request,'students/child_detail/child_detail_pool_update.html')

class Child_detailDownloadProfileView(View):
    @method_decorator(login_required)
    def get(self,request,**kwargs):
        pk=self.kwargs.get('pk')
        school_code = self.kwargs.get('school_code')
        school_id = request.user.account.associated_with
        schl_id = School.objects.get(id=school_id)
        # if request.user.account.user_category_id == 2:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 5:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, block_id=request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code, district_id= request.user.account.associated_with).exclude(transfer_flag = 1)
        # elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
        #     child_detail_list = Child_detail.objects.filter(staff_id=school_code).exclude(transfer_flag = 1)    
        # else:
        child_detail_list = Child_detail.objects.values("name","aadhaar_eid_number","aadhaar_uid_number","gender","dob","community__community_name","religion__religion_name","mothertounge__language_name","phone_number","child_differently_abled","differently_abled","child_disadvantaged_group","disadvantaged_group","subcaste__caste_name","nationality__nationality","house_address","native_district","pin_code","blood_group","mother_name","mother_occupation","father_name","father_occupation","parent_income","class_studying__class_studying","group_code__group_name","attendance_status","sport_participation","education_medium__education_medium","district__district_name","block__block_name","unique_id_no","school_id","staff_id","bank__bank","bank_account_no","schemes","academic_year__academic_year","transfer_flag","transfer_date","name_tamil","class_section","student_admitted_section","school_admission_no","bank_ifsc_code","sports_player","sports_name","community_certificate","child_status","height","weight","laptop_issued","laptop_slno","guardian_name").filter(staff_id=schl_id.school_code,class_studying_id=pk).exclude(transfer_flag = 1).order_by('name')
        data = [['Name of the Student', 'Unique ID No', 'Class Studying', 'Section', 'Academic Year', 'Gender', 'Date of Birth', 'Community', 'Subcaste', 'Religion', 'Fathers Name', 'Mothers Name', 'Guardian Name', 'Address', 'Mother Tongue', 'Phone Number', 'Child Differently Abled', 'If yes', 'Child Disadvantaged Group', 'If yes', 'Aadhaar Eid Number', 'Aadhaar Uid Number'
                , 'Nationality', 'Native District', 'Pincode', 'Blood Group', 'Mothers Occupation', 'Fathers Occupation', 'Parent Income', 'Attendance Status', 'Sport Participation', 'Education Medium', 'Bank Account No', 'Bank Ifsc Code', 'If Yes', 'Student Admitted Section', 'School Admission No', 'Sports Player', 'Sports Name', 'Community Certificate'
                , 'Child Status', 'Height (cm)', 'Weight (kg)', 'Laptop Issued', 'Laptop Slno']]
        for i in child_detail_list:
            data.append([i['name'], i['unique_id_no'], i['class_studying__class_studying'], i['class_section'], i['academic_year__academic_year'], i['gender'], i['dob'], i['community__community_name'], i['subcaste__caste_name'], i['religion__religion_name'], i['father_name'], i['mother_name'], i['guardian_name'], i['house_address'], i['mothertounge__language_name'], i['phone_number'], i['child_differently_abled'], i['differently_abled'], i['child_disadvantaged_group'], i['disadvantaged_group'], i['aadhaar_eid_number'], i['aadhaar_uid_number']
                , i['nationality__nationality'], i['native_district'], i['pin_code'], i['blood_group'], i['mother_occupation'], i['father_occupation'], i['parent_income'], i['attendance_status'], i['sport_participation'], i['education_medium__education_medium'], i['bank_account_no'], i['bank_ifsc_code'], i['schemes']
                , i['student_admitted_section'], i['school_admission_no'], i['sports_player'], i['sports_name'], i['community_certificate'], i['child_status'], i['height'], i['weight'], i['laptop_issued'], i['laptop_slno']])
        return ExcelResponse(data, 'Child_Profile')
