from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_family_detail


class Teacher_family_detailView(object):
    model = Teacher_family_detail

    def get_template_names(self):
        """Nest templates within teacher_family_detail directory."""
        tpl = super(Teacher_family_detailView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_family_detail'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_family_detail/'+tpl[8:]
        return [self.template_name]


class Teacher_family_detailDateView(Teacher_family_detailView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailBaseListView(Teacher_family_detailView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailArchiveIndexView(
    Teacher_family_detailDateView, Teacher_family_detailBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailCreateView(Teacher_family_detailView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailDateDetailView(Teacher_family_detailDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailDayArchiveView(
    Teacher_family_detailDateView, Teacher_family_detailBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailDeleteView(Teacher_family_detailView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailDetailView(Teacher_family_detailView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailListView(Teacher_family_detailBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailMonthArchiveView(
    Teacher_family_detailDateView, Teacher_family_detailBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailTodayArchiveView(
    Teacher_family_detailDateView, Teacher_family_detailBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailUpdateView(Teacher_family_detailView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailWeekArchiveView(
    Teacher_family_detailDateView, Teacher_family_detailBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')


class Teacher_family_detailYearArchiveView(
    Teacher_family_detailDateView, Teacher_family_detailBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_family_detail_list')



