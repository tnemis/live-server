from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_action


class Teacher_actionView(object):
    model = Teacher_action

    def get_template_names(self):
        """Nest templates within teacher_action directory."""
        tpl = super(Teacher_actionView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_action'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_action/'+tpl[8:]
        return [self.template_name]


class Teacher_actionDateView(Teacher_actionView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionBaseListView(Teacher_actionView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionArchiveIndexView(
    Teacher_actionDateView, Teacher_actionBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionCreateView(Teacher_actionView, CreateView):
    pass
    # import ipdb;ipdb.set_trace()
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionDateDetailView(Teacher_actionDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionDayArchiveView(
    Teacher_actionDateView, Teacher_actionBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionDeleteView(Teacher_actionView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionDetailView(Teacher_actionView, DetailView):
    pass


    def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('teacher_teacher_action_list')

class Teacher_actionListView(Teacher_actionBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionMonthArchiveView(
    Teacher_actionDateView, Teacher_actionBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionTodayArchiveView(
    Teacher_actionDateView, Teacher_actionBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionUpdateView(Teacher_actionView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionWeekArchiveView(
    Teacher_actionDateView, Teacher_actionBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')


class Teacher_actionYearArchiveView(
    Teacher_actionDateView, Teacher_actionBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_action_list')



