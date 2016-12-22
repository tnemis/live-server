from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Education_medium


class Education_mediumView(object):
    model = Education_medium

    def get_template_names(self):
        """Nest templates within education_medium directory."""
        tpl = super(Education_mediumView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'education_medium'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Education_mediumDateView(Education_mediumView):
    date_field = 'created_date'
    month_format = '%m'


class Education_mediumBaseListView(Education_mediumView):
    paginate_by = 10


class Education_mediumArchiveIndexView(
    Education_mediumDateView, Education_mediumBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumCreateView(Education_mediumView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumDateDetailView(Education_mediumDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumDayArchiveView(
    Education_mediumDateView, Education_mediumBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumDeleteView(Education_mediumView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumDetailView(Education_mediumView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumListView(Education_mediumBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumMonthArchiveView(
    Education_mediumDateView, Education_mediumBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumTodayArchiveView(
    Education_mediumDateView, Education_mediumBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumUpdateView(Education_mediumView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumWeekArchiveView(
    Education_mediumDateView, Education_mediumBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_education_medium_list')


class Education_mediumYearArchiveView(
    Education_mediumDateView, Education_mediumBaseListView, YearArchiveView):
    make_object_list = True



