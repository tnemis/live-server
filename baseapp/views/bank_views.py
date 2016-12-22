from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Bank
from django.contrib import auth, messages



class BankView(object):
    model = Bank

    def get_template_names(self):
        """Nest templates within bank directory."""
        tpl = super(BankView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'bank'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class BankDateView(BankView):
    date_field = 'created_date'
    month_format = '%m'


class BankBaseListView(BankView):
    paginate_by = 10


class BankArchiveIndexView(
    BankDateView, BankBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankCreateView(BankView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_bank_list')


class BankDateDetailView(BankDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankDayArchiveView(
    BankDateView, BankBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankDeleteView(BankView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankDetailView(BankView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankListView(BankBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankMonthArchiveView(
    BankDateView, BankBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankTodayArchiveView(
    BankDateView, BankBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankUpdateView(BankView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankWeekArchiveView(
    BankDateView, BankBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_bank_list')


class BankYearArchiveView(
    BankDateView, BankBaseListView, YearArchiveView):
    make_object_list = True



