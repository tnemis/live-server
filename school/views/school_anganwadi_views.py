from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_anganwadi


class School_anganwadiView(object):
    model = School_anganwadi

    def get_template_names(self):
        """Nest templates within school_anganwadi directory."""
        tpl = super(School_anganwadiView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_anganwadi'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_anganwadi/'+tpl[7:]
        return [self.template_name]


class School_anganwadiDateView(School_anganwadiView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiBaseListView(School_anganwadiView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiArchiveIndexView(
    School_anganwadiDateView, School_anganwadiBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiCreateView(School_anganwadiView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiDateDetailView(School_anganwadiDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiDayArchiveView(
    School_anganwadiDateView, School_anganwadiBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiDeleteView(School_anganwadiView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiDetailView(School_anganwadiView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiListView(School_anganwadiBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiMonthArchiveView(
    School_anganwadiDateView, School_anganwadiBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiTodayArchiveView(
    School_anganwadiDateView, School_anganwadiBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiUpdateView(School_anganwadiView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiWeekArchiveView(
    School_anganwadiDateView, School_anganwadiBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')


class School_anganwadiYearArchiveView(
    School_anganwadiDateView, School_anganwadiBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_anganwadi_list')



