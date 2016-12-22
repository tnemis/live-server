from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_flag


class School_flagView(object):
    model = School_flag

    def get_template_names(self):
        """Nest templates within school_flag directory."""
        tpl = super(School_flagView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_flag'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_flag/'+tpl[7:]
        return [self.template_name]


class School_flagDateView(School_flagView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagBaseListView(School_flagView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagArchiveIndexView(
    School_flagDateView, School_flagBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagCreateView(School_flagView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagDateDetailView(School_flagDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagDayArchiveView(
    School_flagDateView, School_flagBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagDeleteView(School_flagView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagDetailView(School_flagView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagListView(School_flagBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagMonthArchiveView(
    School_flagDateView, School_flagBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagTodayArchiveView(
    School_flagDateView, School_flagBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagUpdateView(School_flagView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagWeekArchiveView(
    School_flagDateView, School_flagBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')


class School_flagYearArchiveView(
    School_flagDateView, School_flagBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_flag_list')



