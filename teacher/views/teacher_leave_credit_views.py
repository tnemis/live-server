from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_leave_credit


class Teacher_leave_creditView(object):
    model = Teacher_leave_credit

    def get_template_names(self):
        """Nest templates within teacher_leave_credit directory."""
        tpl = super(Teacher_leave_creditView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_leave_credit'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_leave_credit/'+tpl[8:]
        return [self.template_name]


class Teacher_leave_creditDateView(Teacher_leave_creditView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditBaseListView(Teacher_leave_creditView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditArchiveIndexView(
    Teacher_leave_creditDateView, Teacher_leave_creditBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditCreateView(Teacher_leave_creditView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditDateDetailView(Teacher_leave_creditDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditDayArchiveView(
    Teacher_leave_creditDateView, Teacher_leave_creditBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditDeleteView(Teacher_leave_creditView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditDetailView(Teacher_leave_creditView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditListView(Teacher_leave_creditBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditMonthArchiveView(
    Teacher_leave_creditDateView, Teacher_leave_creditBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditTodayArchiveView(
    Teacher_leave_creditDateView, Teacher_leave_creditBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditUpdateView(Teacher_leave_creditView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditWeekArchiveView(
    Teacher_leave_creditDateView, Teacher_leave_creditBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')


class Teacher_leave_creditYearArchiveView(
    Teacher_leave_creditDateView, Teacher_leave_creditBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_credit_list')



