from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_contact_detail


class School_contact_detailView(object):
    model = School_contact_detail

    def get_template_names(self):
        """Nest templates within school_contact_detail directory."""
        tpl = super(School_contact_detailView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_contact_detail'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_contact_detail/'+tpl[7:]
        return [self.template_name]


class School_contact_detailDateView(School_contact_detailView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailBaseListView(School_contact_detailView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailArchiveIndexView(
    School_contact_detailDateView, School_contact_detailBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailCreateView(School_contact_detailView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailDateDetailView(School_contact_detailDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailDayArchiveView(
    School_contact_detailDateView, School_contact_detailBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailDeleteView(School_contact_detailView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')


class School_contact_detailDetailView(School_contact_detailView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailListView(School_contact_detailBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailMonthArchiveView(
    School_contact_detailDateView, School_contact_detailBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailTodayArchiveView(
    School_contact_detailDateView, School_contact_detailBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailUpdateView(School_contact_detailView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailWeekArchiveView(
    School_contact_detailDateView, School_contact_detailBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')



class School_contact_detailYearArchiveView(
    School_contact_detailDateView, School_contact_detailBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_contact_detail_list')




