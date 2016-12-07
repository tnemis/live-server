from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Academic_Year
from django.contrib import auth, messages


class Academic_YearView(object):
    model = Academic_Year

    def get_template_names(self):
        """Nest templates within academic_year directory."""
        tpl = super(Academic_YearView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'academic_year'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Academic_YearDateView(Academic_YearView):
    date_field = 'created_date'
    month_format = '%m'


class Academic_YearBaseListView(Academic_YearView):
    paginate_by = 10


class Academic_YearArchiveIndexView(
    Academic_YearDateView, Academic_YearBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearCreateView(Academic_YearView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_academic_year_list')


class Academic_YearDateDetailView(Academic_YearDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearDayArchiveView(
    Academic_YearDateView, Academic_YearBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearDeleteView(Academic_YearView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearDetailView(Academic_YearView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearListView(Academic_YearBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearMonthArchiveView(
    Academic_YearDateView, Academic_YearBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearTodayArchiveView(
    Academic_YearDateView, Academic_YearBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearUpdateView(Academic_YearView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearWeekArchiveView(
    Academic_YearDateView, Academic_YearBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_academic_year_list')


class Academic_YearYearArchiveView(
    Academic_YearDateView, Academic_YearBaseListView, YearArchiveView):
    make_object_list = True



