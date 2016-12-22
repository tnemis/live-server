from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from students.models import Child_Transfer_History


class Child_Transfer_HistoryView(object):
    model = Child_Transfer_History

    def get_template_names(self):
        """Nest templates within child_transfer_history directory."""
        tpl = super(Child_Transfer_HistoryView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'child_transfer_history'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Child_Transfer_HistoryDateView(Child_Transfer_HistoryView):
    date_field = 'tc_issue_date'
    month_format = '%m'


class Child_Transfer_HistoryBaseListView(Child_Transfer_HistoryView):
    paginate_by = 10


class Child_Transfer_HistoryArchiveIndexView(
    Child_Transfer_HistoryDateView, Child_Transfer_HistoryBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryCreateView(Child_Transfer_HistoryView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryDateDetailView(Child_Transfer_HistoryDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryDayArchiveView(
    Child_Transfer_HistoryDateView, Child_Transfer_HistoryBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryDeleteView(Child_Transfer_HistoryView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryDetailView(Child_Transfer_HistoryView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryListView(Child_Transfer_HistoryBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryMonthArchiveView(
    Child_Transfer_HistoryDateView, Child_Transfer_HistoryBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryTodayArchiveView(
    Child_Transfer_HistoryDateView, Child_Transfer_HistoryBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryUpdateView(Child_Transfer_HistoryView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryWeekArchiveView(
    Child_Transfer_HistoryDateView, Child_Transfer_HistoryBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_transfer_history_list')


class Child_Transfer_HistoryYearArchiveView(
    Child_Transfer_HistoryDateView, Child_Transfer_HistoryBaseListView, YearArchiveView):
    make_object_list = True



