from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Sub_Castes
from django.contrib import auth, messages


class Sub_CastesView(object):
    model = Sub_Castes

    def get_template_names(self):
        """Nest templates within sub_castes directory."""
        tpl = super(Sub_CastesView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'sub_castes'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Sub_CastesDateView(Sub_CastesView):
    date_field = 'created_date'
    month_format = '%m'


class Sub_CastesBaseListView(Sub_CastesView):
    paginate_by = 10


class Sub_CastesArchiveIndexView(
    Sub_CastesDateView, Sub_CastesBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesCreateView(Sub_CastesView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_sub_castes_list')


class Sub_CastesDateDetailView(Sub_CastesDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesDayArchiveView(
    Sub_CastesDateView, Sub_CastesBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesDeleteView(Sub_CastesView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesDetailView(Sub_CastesView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesListView(Sub_CastesBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesMonthArchiveView(
    Sub_CastesDateView, Sub_CastesBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesTodayArchiveView(
    Sub_CastesDateView, Sub_CastesBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesUpdateView(Sub_CastesView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesWeekArchiveView(
    Sub_CastesDateView, Sub_CastesBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_sub_castes_list')


class Sub_CastesYearArchiveView(
    Sub_CastesDateView, Sub_CastesBaseListView, YearArchiveView):
    make_object_list = True



