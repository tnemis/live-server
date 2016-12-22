from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_education


class Teacher_educationView(object):
    model = Teacher_education

    def get_template_names(self):
        """Nest templates within teacher_education directory."""
        tpl = super(Teacher_educationView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_education'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_education/'+tpl[8:]
        return [self.template_name]


class Teacher_educationDateView(Teacher_educationView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationBaseListView(Teacher_educationView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationArchiveIndexView(
    Teacher_educationDateView, Teacher_educationBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationCreateView(Teacher_educationView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationDateDetailView(Teacher_educationDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationDayArchiveView(
    Teacher_educationDateView, Teacher_educationBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationDeleteView(Teacher_educationView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')


class Teacher_educationDetailView(Teacher_educationView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationListView(Teacher_educationBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationMonthArchiveView(
    Teacher_educationDateView, Teacher_educationBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationTodayArchiveView(
    Teacher_educationDateView, Teacher_educationBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationUpdateView(Teacher_educationView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationWeekArchiveView(
    Teacher_educationDateView, Teacher_educationBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')



class Teacher_educationYearArchiveView(
    Teacher_educationDateView, Teacher_educationBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_education_list')




