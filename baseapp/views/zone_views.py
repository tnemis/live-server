from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Zone
from django.contrib import auth, messages


class ZoneView(object):
    model = Zone

    def get_template_names(self):
        """Nest templates within zone directory."""
        tpl = super(ZoneView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'zone'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ZoneDateView(ZoneView):
    date_field = 'created_date'
    month_format = '%m'


class ZoneBaseListView(ZoneView):
    paginate_by = 10


class ZoneArchiveIndexView(
    ZoneDateView, ZoneBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneCreateView(ZoneView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_zone_list')



class ZoneDateDetailView(ZoneDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneDayArchiveView(
    ZoneDateView, ZoneBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneDeleteView(ZoneView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')


class ZoneDetailView(ZoneView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneListView(ZoneBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneMonthArchiveView(
    ZoneDateView, ZoneBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneTodayArchiveView(
    ZoneDateView, ZoneBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneUpdateView(ZoneView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneWeekArchiveView(
    ZoneDateView, ZoneBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_zone_list')



class ZoneYearArchiveView(
    ZoneDateView, ZoneBaseListView, YearArchiveView):
    make_object_list = True



