from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_test


class Teacher_testView(object):
    model = Teacher_test

    def get_template_names(self):
        """Nest templates within teacher_test directory."""
        tpl = super(Teacher_testView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_test'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_test/'+tpl[8:]
        return [self.template_name]


class Teacher_testDateView(Teacher_testView):
    date_field = 'timestamp'
    month_format = '%m'


class Teacher_testBaseListView(Teacher_testView):
    paginate_by = 10


class Teacher_testArchiveIndexView(
    Teacher_testDateView, Teacher_testBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testCreateView(Teacher_testView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testDateDetailView(Teacher_testDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testDayArchiveView(
    Teacher_testDateView, Teacher_testBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testDeleteView(Teacher_testView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testDetailView(Teacher_testView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testListView(Teacher_testBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testMonthArchiveView(
    Teacher_testDateView, Teacher_testBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testTodayArchiveView(
    Teacher_testDateView, Teacher_testBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testUpdateView(Teacher_testView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testWeekArchiveView(
    Teacher_testDateView, Teacher_testBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')


class Teacher_testYearArchiveView(
    Teacher_testDateView, Teacher_testBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_test_list')



