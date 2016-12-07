from django.views.generic import View,ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_personal_detail


from django.shortcuts import render

from baseapp.models import District, School, Habitation, Zone, Schemes, Class_Studying, Differently_abled, Disadvantaged_group, Child_detail_pool_database, Language, Block
from django.contrib import messages
from teacher.forms import Teacher_personal_detailform, Teacher_personal_detail_Poolform
from django.db import connection
from datetime import datetime





class Teacher_personal_detailView(object):
    model = Teacher_personal_detail

    def get_template_names(self):
        """Nest templates within teacher_personal_detail directory."""
        #import ipdb; ipdb.set_trace()
        tpl = super(Teacher_personal_detailView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_personal_detail'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_personal_detail/'+tpl[8:]
        return [self.template_name]


class Teacher_personal_detailDateView(Teacher_personal_detailView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailBaseListView(Teacher_personal_detailView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailArchiveIndexView(
    Teacher_personal_detailDateView, Teacher_personal_detailBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailCreateView(Teacher_personal_detailView, CreateView):
    
    pass
    # import ipdb;ipdb.set_trace()
    def get_success_url(self):
        # language_list = Language.objects.all().order_by('language_name')
        # form=Teacher_personal_detailform()
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')
        # return render (request,'teacher/teacher_personal_detail/teacher_personal_detail_form.html',{'language_list':language_list,'form':form})


class Teacher_personal_detailDateDetailView(Teacher_personal_detailDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailDayArchiveView(
    Teacher_personal_detailDateView, Teacher_personal_detailBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailDeleteView(Teacher_personal_detailView, DeleteView):


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailDetailView(Teacher_personal_detailView, DetailView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')

class Teacher_personal_detailListView(View):

    def get(self,request,**kwargs):

        try:
            school_code = self.request.GET.get('school_code')
            if request.user.account.user_category_id == 2:
                child_detail_list = School_child_count.objects.get(school__school_code=school_code, school__block_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 5:
                child_detail_list = School_child_count.objects.get(school__school_code=school_code, school__block_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 6 or request.user.account.user_category_id == 7 or request.user.account.user_category_id == 8 or request.user.account.user_category_id == 12 or request.user.account.user_category_id == 13 or request.user.account.user_category_id == 14:
                child_detail_list = School_child_count.objects.get(school__school_code=school_code, school__district_id= request.user.account.associated_with)
            elif request.user.account.user_category_id == 9 or request.user.account.user_category_id == 10 or request.user.account.user_category_id == 11 or request.user.account.user_category_id == 15 or request.user.account.user_category_id == 16 or request.user.account.user_category_id == 17 or request.user.account.user_category_id == 4:
                child_detail_list = School_child_count.objects.get(school__school_code=school_code)    
            else:
                teacher_detail_list = Teacher_personal_detail.objects.filter(school_id=request.user.account.associated_with)


            return render(request,'teacher/teacher_personal_detail/teacher_personal_detail_list.html',{'object_list':teacher_detail_list,'school_code':school_code})
        except Teacher_personal_detail.DoesNotExist:
            messages.add_message(
                self.request,
                messages.ERROR,"No Teacher Data"
            )
            return render(request,'teacher/teacher_personal_detail/teacher_personal_detail_list.html',locals())


class Teacher_personal_detailMonthArchiveView(
    Teacher_personal_detailDateView, Teacher_personal_detailBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailTodayArchiveView(
    Teacher_personal_detailDateView, Teacher_personal_detailBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailUpdateView(Teacher_personal_detailView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')



class Teacher_personal_detailWeekArchiveView(
    Teacher_personal_detailDateView, Teacher_personal_detailBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailYearArchiveView(
    Teacher_personal_detailDateView, Teacher_personal_detailBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_personal_detail_list')


class Teacher_personal_detailPoolView(View):
    def get(self,request,**kwargs):
        form = Teacher_personal_detail_Poolform()
        return render(request,'teacher/teacher_personal_detail/teacher_personal_detail_gpf_no_search.html',locals())
        
    def post(self,request,**kwargs):
        form = Teacher_personal_detail_Poolform()
        tchr_detail = Teacher_personal_detail.objects.filter(school_id=0)
        if request.POST['gpf_no']:
            gpf_no = request.POST['gpf_no']
            teacher_detail = tchr_detail.filter(gpf_no=gpf_no)
        elif request.POST['name'] or request.POST['dob']:
            name =  request.POST['name']
            dob = datetime.strptime(request.POST['dob'], '%d/%m/%Y').strftime('%Y-%m-%d')
            teacher_detail = tchr_detail.filter(name=name,dob=dob)
        return render(request,'teacher/teacher_personal_detail/teacher_personal_detail_gpf_no_search.html',{'teacher_detail':teacher_detail,'form':form})

class Teacher_personal_detailPoolUpdateView(View):

    def get(self,request,**kwargs):
        teacher_id = self.kwargs.get('pk')
        teacher_detail = Teacher_personal_detail.objects.get(id=teacher_id)
        
        return render(request,'teacher/teacher_personal_detail/teacher_personal_detail_pool_update.html',{'teacher_detail':teacher_detail})
    def post(self,request,**kwargs):
        teacher_id = self.kwargs.get('pk')
        school_code = request.POST.get('school_id')
        school_id = School.objects.get(school_code=school_code)
        cur1 = connection.cursor()
        cur1.execute("update teacher_teacher_personal_detail set school_id=%s where id=%s"%(school_id.id,teacher_id))

        return render(request,'teacher/teacher_personal_detail/teacher_personal_detail_pool_update.html',{'school_id':school_id})