from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_upgradation


class School_upgradationView(object):
    model = School_upgradation

    def get_template_names(self):
        """Nest templates within school_upgradation directory."""
        tpl = super(School_upgradationView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_upgradation'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_upgradation/'+tpl[7:]
        return [self.template_name]


class School_upgradationDateView(School_upgradationView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationBaseListView(School_upgradationView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationArchiveIndexView(
    School_upgradationDateView, School_upgradationBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationCreateView(School_upgradationView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationDateDetailView(School_upgradationDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationDayArchiveView(
    School_upgradationDateView, School_upgradationBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationDeleteView(School_upgradationView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationDetailView(School_upgradationView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationListView(School_upgradationBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationMonthArchiveView(
    School_upgradationDateView, School_upgradationBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationTodayArchiveView(
    School_upgradationDateView, School_upgradationBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationUpdateView(School_upgradationView, UpdateView):
    pass


    def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('school_school_upgradation_list')

class School_upgradationWeekArchiveView(
    School_upgradationDateView, School_upgradationBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')


class School_upgradationYearArchiveView(
    School_upgradationDateView, School_upgradationBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_upgradation_list')



