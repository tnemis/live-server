from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_previous_employment


class Teacher_previous_employmentView(object):
    model = Teacher_previous_employment

    def get_template_names(self):
        """Nest templates within teacher_previous_employment directory."""
        tpl = super(Teacher_previous_employmentView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_previous_employment'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_previous_employment/'+tpl[8:]
        return [self.template_name]


class Teacher_previous_employmentDateView(Teacher_previous_employmentView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentBaseListView(Teacher_previous_employmentView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentArchiveIndexView(
    Teacher_previous_employmentDateView, Teacher_previous_employmentBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentCreateView(Teacher_previous_employmentView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentDateDetailView(Teacher_previous_employmentDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentDayArchiveView(
    Teacher_previous_employmentDateView, Teacher_previous_employmentBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentDeleteView(Teacher_previous_employmentView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentDetailView(Teacher_previous_employmentView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentListView(Teacher_previous_employmentBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentMonthArchiveView(
    Teacher_previous_employmentDateView, Teacher_previous_employmentBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentTodayArchiveView(
    Teacher_previous_employmentDateView, Teacher_previous_employmentBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentUpdateView(Teacher_previous_employmentView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentWeekArchiveView(
    Teacher_previous_employmentDateView, Teacher_previous_employmentBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')


class Teacher_previous_employmentYearArchiveView(
    Teacher_previous_employmentDateView, Teacher_previous_employmentBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_previous_employment_list')



