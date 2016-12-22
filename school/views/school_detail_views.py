from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_detail


class School_detailView(object):
    model = School_detail

    def get_template_names(self):
        """Nest templates within school_detail directory."""
        tpl = super(School_detailView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_detail'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_detail/'+tpl[7:]
        return [self.template_name]


class School_detailDateView(School_detailView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailBaseListView(School_detailView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailArchiveIndexView(
    School_detailDateView, School_detailBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailCreateView(School_detailView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailDateDetailView(School_detailDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailDayArchiveView(
    School_detailDateView, School_detailBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailDeleteView(School_detailView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailDetailView(School_detailView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailListView(School_detailBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailMonthArchiveView(
    School_detailDateView, School_detailBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailTodayArchiveView(
    School_detailDateView, School_detailBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailUpdateView(School_detailView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailWeekArchiveView(
    School_detailDateView, School_detailBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')


class School_detailYearArchiveView(
    School_detailDateView, School_detailBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_detail_list')



