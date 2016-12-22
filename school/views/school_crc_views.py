from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_crc


class School_crcView(object):
    model = School_crc

    def get_template_names(self):
        """Nest templates within school_crc directory."""
        tpl = super(School_crcView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_crc'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_crc/'+tpl[7:]
        return [self.template_name]


class School_crcDateView(School_crcView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcBaseListView(School_crcView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcArchiveIndexView(
    School_crcDateView, School_crcBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcCreateView(School_crcView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcDateDetailView(School_crcDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcDayArchiveView(
    School_crcDateView, School_crcBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcDeleteView(School_crcView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcDetailView(School_crcView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcListView(School_crcBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcMonthArchiveView(
    School_crcDateView, School_crcBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcTodayArchiveView(
    School_crcDateView, School_crcBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcUpdateView(School_crcView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcWeekArchiveView(
    School_crcDateView, School_crcBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')


class School_crcYearArchiveView(
    School_crcDateView, School_crcBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_crc_list')



