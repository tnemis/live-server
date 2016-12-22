from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_leave_surrender


class Teacher_leave_surrenderView(object):
    model = Teacher_leave_surrender

    def get_template_names(self):
        """Nest templates within teacher_leave_surrender directory."""
        tpl = super(Teacher_leave_surrenderView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_leave_surrender'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_leave_surrender/'+tpl[8:]
        return [self.template_name]


class Teacher_leave_surrenderDateView(Teacher_leave_surrenderView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderBaseListView(Teacher_leave_surrenderView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderArchiveIndexView(
    Teacher_leave_surrenderDateView, Teacher_leave_surrenderBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderCreateView(Teacher_leave_surrenderView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderDateDetailView(Teacher_leave_surrenderDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderDayArchiveView(
    Teacher_leave_surrenderDateView, Teacher_leave_surrenderBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderDeleteView(Teacher_leave_surrenderView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderDetailView(Teacher_leave_surrenderView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderListView(Teacher_leave_surrenderBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderMonthArchiveView(
    Teacher_leave_surrenderDateView, Teacher_leave_surrenderBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderTodayArchiveView(
    Teacher_leave_surrenderDateView, Teacher_leave_surrenderBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderUpdateView(Teacher_leave_surrenderView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderWeekArchiveView(
    Teacher_leave_surrenderDateView, Teacher_leave_surrenderBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')


class Teacher_leave_surrenderYearArchiveView(
    Teacher_leave_surrenderDateView, Teacher_leave_surrenderBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_surrender_list')



