from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_nomini


class Teacher_nominiView(object):
    model = Teacher_nomini

    def get_template_names(self):
        """Nest templates within teacher_nomini directory."""
        tpl = super(Teacher_nominiView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_nomini'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_nomini/'+tpl[8:]
        return [self.template_name]


class Teacher_nominiDateView(Teacher_nominiView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiBaseListView(Teacher_nominiView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiArchiveIndexView(
    Teacher_nominiDateView, Teacher_nominiBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiCreateView(Teacher_nominiView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiDateDetailView(Teacher_nominiDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiDayArchiveView(
    Teacher_nominiDateView, Teacher_nominiBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiDeleteView(Teacher_nominiView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiDetailView(Teacher_nominiView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiListView(Teacher_nominiBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiMonthArchiveView(
    Teacher_nominiDateView, Teacher_nominiBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiTodayArchiveView(
    Teacher_nominiDateView, Teacher_nominiBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiUpdateView(Teacher_nominiView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiWeekArchiveView(
    Teacher_nominiDateView, Teacher_nominiBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')


class Teacher_nominiYearArchiveView(
    Teacher_nominiDateView, Teacher_nominiBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_nomini_list')



