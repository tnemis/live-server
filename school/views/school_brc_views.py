from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_brc


class School_brcView(object):
    model = School_brc

    def get_template_names(self):
        """Nest templates within school_brc directory."""
        tpl = super(School_brcView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_brc'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_brc/'+tpl[7:]
        return [self.template_name]


class School_brcDateView(School_brcView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcBaseListView(School_brcView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcArchiveIndexView(
    School_brcDateView, School_brcBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcCreateView(School_brcView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcDateDetailView(School_brcDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcDayArchiveView(
    School_brcDateView, School_brcBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcDeleteView(School_brcView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcDetailView(School_brcView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcListView(School_brcBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcMonthArchiveView(
    School_brcDateView, School_brcBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcTodayArchiveView(
    School_brcDateView, School_brcBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcUpdateView(School_brcView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcWeekArchiveView(
    School_brcDateView, School_brcBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')


class School_brcYearArchiveView(
    School_brcDateView, School_brcBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_brc_list')



