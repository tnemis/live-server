from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_leave


class Teacher_leaveView(object):
    model = Teacher_leave

    def get_template_names(self):
        """Nest templates within teacher_leave directory."""
        tpl = super(Teacher_leaveView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_leave'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_leave/'+tpl[8:]
        return [self.template_name]


class Teacher_leaveDateView(Teacher_leaveView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveBaseListView(Teacher_leaveView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveArchiveIndexView(
    Teacher_leaveDateView, Teacher_leaveBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveCreateView(Teacher_leaveView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveDateDetailView(Teacher_leaveDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveDayArchiveView(
    Teacher_leaveDateView, Teacher_leaveBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveDeleteView(Teacher_leaveView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveDetailView(Teacher_leaveView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveListView(Teacher_leaveBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveMonthArchiveView(
    Teacher_leaveDateView, Teacher_leaveBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveTodayArchiveView(
    Teacher_leaveDateView, Teacher_leaveBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveUpdateView(Teacher_leaveView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveWeekArchiveView(
    Teacher_leaveDateView, Teacher_leaveBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')


class Teacher_leaveYearArchiveView(
    Teacher_leaveDateView, Teacher_leaveBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_leave_list')



