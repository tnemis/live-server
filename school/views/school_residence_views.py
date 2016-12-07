from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_residence


class School_residenceView(object):
    model = School_residence

    def get_template_names(self):
        """Nest templates within school_residence directory."""
        tpl = super(School_residenceView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_residence'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_residence/'+tpl[7:]
        return [self.template_name]


class School_residenceDateView(School_residenceView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceBaseListView(School_residenceView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceArchiveIndexView(
    School_residenceDateView, School_residenceBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceCreateView(School_residenceView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceDateDetailView(School_residenceDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceDayArchiveView(
    School_residenceDateView, School_residenceBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceDeleteView(School_residenceView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceDetailView(School_residenceView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceListView(School_residenceBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceMonthArchiveView(
    School_residenceDateView, School_residenceBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceTodayArchiveView(
    School_residenceDateView, School_residenceBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceUpdateView(School_residenceView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceWeekArchiveView(
    School_residenceDateView, School_residenceBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')


class School_residenceYearArchiveView(
    School_residenceDateView, School_residenceBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_residence_list')



