from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Nationality


class NationalityView(object):
    model = Nationality

    def get_template_names(self):
        """Nest templates within nationality directory."""
        tpl = super(NationalityView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'nationality'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class NationalityDateView(NationalityView):
    date_field = 'created_date'
    month_format = '%m'


class NationalityBaseListView(NationalityView):
    paginate_by = 10


class NationalityArchiveIndexView(
    NationalityDateView, NationalityBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityCreateView(NationalityView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityDateDetailView(NationalityDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityDayArchiveView(
    NationalityDateView, NationalityBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityDeleteView(NationalityView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityDetailView(NationalityView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityListView(NationalityBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityMonthArchiveView(
    NationalityDateView, NationalityBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityTodayArchiveView(
    NationalityDateView, NationalityBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityUpdateView(NationalityView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityWeekArchiveView(
    NationalityDateView, NationalityBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_nationality_list')


class NationalityYearArchiveView(
    NationalityDateView, NationalityBaseListView, YearArchiveView):
    make_object_list = True



