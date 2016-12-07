from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView, View


from school.models import School_info
from baseapp.models import School, Block
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class SchoolView(object):
    model = School_info

    def get_template_names(self):
        """Nest templates within school directory."""
        tpl = super(SchoolView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school/'+tpl[7:]
        return [self.template_name]


class SchoolDateView(SchoolView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolBaseListView(SchoolView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolArchiveIndexView(
    SchoolDateView, SchoolBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolCreateView(SchoolView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolDateDetailView(SchoolDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolDayArchiveView(
    SchoolDateView, SchoolBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolDeleteView(SchoolView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')

class SchoolDetailView(View):
    def get(self,request,**kwargs):
        pk = self.kwargs.get('pk')
        try:
            school_detail = School_info.objects.get(school_id=pk)
            return render(request,'school/school/object_table_detail.html',{'object':school_detail})
        except School_info.DoesNotExist:
            message="Yet school is not update"
            return render(request,'school/school/object_table_detail.html',{'message':message})
       
    
class SchoolListView(View):
    def get(self,request,**kwargs):
        if request.user.account.user_category_id == 1:
            try:
                school_detail = School_info.objects.get(school_id=request.user.account.associated_with)
                return render(request,'school/school/object_table_detail.html',{'object':school_detail})
            except School_info.DoesNotExist:
                return render(request,'school/school/object_table_detail.html')
        else:
            if request.user.account.user_category_id == 2:
                school_list = School.objects.filter(block__id=request.user.account.associated_with, category_id__in=[1,2,4])
            elif request.user.account.user_category_id == 5:
                school_list = School.objects.filter(block__id=request.user.account.associated_with, category_id__in=[3,5,6,7,8,9,10])
            elif request.user.account.user_category_id == 6:
                school_list = School.objects.filter(district__id=request.user.account.associated_with, management_id__in=[1,2,6,8,7,4,5], category_id__in=[1,2,4,12,11])
            elif request.user.account.user_category_id == 7:
                school_list = School.objects.filter(district__id=request.user.account.associated_with, management_id__in=[1,2,6,8,7,4,5], category_id__in=[3,5,6,7,8,9,10])
            elif request.user.account.user_category_id == 8:
                school_list = School.objects.filter(district__id=request.user.account.associated_with, management_id=9)
            elif request.user.account.user_category_id == 9:
                school_list = School.objects.filter(management_id__in=[1,2,6,8,7,4,5], category_id__in=[1,2,4,12,11])
            elif request.user.account.user_category_id == 10:
                school_list = School.objects.filter(management_id__in=[1,2,6,8,7,4,5], category_id__in=[3,5,6,7,8,9,10])
            elif request.user.account.user_category_id == 11:
                school_list = School.objects.filter(management_id=9)
            elif request.user.account.user_category_id == 12:
                school_list = School.objects.filter(district__id=request.user.account.associated_with, management_id=10)
            elif request.user.account.user_category_id == 13:
                school_list = School.objects.filter(district__id=request.user.account.associated_with, management_id=11)
            elif request.user.account.user_category_id == 14:
                school_list = School.objects.filter(district__id=request.user.account.associated_with, category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
            elif request.user.account.user_category_id == 15:
                school_list = School.objects.filter(management_id=10)
            elif request.user.account.user_category_id == 16:
                school_list = School.objects.filter(management_id=11)
            elif request.user.account.user_category_id == 17:
                school_list = School.objects.filter(category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
            elif request.user.account.user_category_id == 4:
                school_list = School.objects.filter(category_id__in=[1,2,4])     
     
            paginator = Paginator(school_list, 10)
            page = request.GET.get('page')
            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            return render(request,'school/school/object_table_list.html',{'school_list':school_list,'page_objs':page_obj})
    def post(self,request,**kwargs):
        if request.POST['state_id'] == '1':
            school_list = School.objects.filter(management_id__in=[1,2,6,8,7,4,5], category_id__in=[1,2,4,12,11])
        elif request.POST['state_id'] == '2':
            school_list = School.objects.filter(management_id__in=[1,2,6,8,7,4,5], category_id__in=[3,5,6,7,8,9,10])
        elif request.POST['state_id'] == '3':
            school_list = School.objects.filter(management_id=9)
        elif request.POST['state_id'] == '4':
            school_list = School.objects.filter(management_id=10)
        elif request.POST['state_id'] == '5':
            school_list = School.objects.filter(management_id=11)
        elif request.POST['state_id'] == '6':
            school_list = School.objects.filter(category_id__in=[1,2,4,12,11,3,5,6,7,8,9,10])
        paginator = Paginator(school_list, 10)
        page = request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return render(request,'school/school/statewise_school_list.html',{'school_list':school_list,'page_objs':page_obj})


class SchoolMonthArchiveView(
    SchoolDateView, SchoolBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolTodayArchiveView(
    SchoolDateView, SchoolBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolUpdateView(SchoolView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolWeekArchiveView(
    SchoolDateView, SchoolBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')


class SchoolYearArchiveView(
    SchoolDateView, SchoolBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_list')



