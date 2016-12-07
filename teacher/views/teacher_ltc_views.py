from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_ltc


class Teacher_ltcView(object):
    model = Teacher_ltc

    def get_template_names(self):
        """Nest templates within teacher_ltc directory."""
        tpl = super(Teacher_ltcView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_ltc'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_ltc/'+tpl[8:]
        return [self.template_name]


class Teacher_ltcDateView(Teacher_ltcView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcBaseListView(Teacher_ltcView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcArchiveIndexView(
    Teacher_ltcDateView, Teacher_ltcBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcCreateView(Teacher_ltcView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcDateDetailView(Teacher_ltcDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcDayArchiveView(
    Teacher_ltcDateView, Teacher_ltcBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcDeleteView(Teacher_ltcView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcDetailView(Teacher_ltcView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcListView(Teacher_ltcBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcMonthArchiveView(
    Teacher_ltcDateView, Teacher_ltcBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcTodayArchiveView(
    Teacher_ltcDateView, Teacher_ltcBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcUpdateView(Teacher_ltcView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcWeekArchiveView(
    Teacher_ltcDateView, Teacher_ltcBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')


class Teacher_ltcYearArchiveView(
    Teacher_ltcDateView, Teacher_ltcBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_ltc_list')



