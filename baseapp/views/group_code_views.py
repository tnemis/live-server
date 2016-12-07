from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Group_code
from django.contrib import auth, messages


class Group_codeView(object):
    model = Group_code

    def get_template_names(self):
        """Nest templates within group_code directory."""
        tpl = super(Group_codeView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'group_code'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Group_codeDateView(Group_codeView):
    date_field = 'created_date'
    month_format = '%m'


class Group_codeBaseListView(Group_codeView):
    paginate_by = 10


class Group_codeArchiveIndexView(
    Group_codeDateView, Group_codeBaseListView, ArchiveIndexView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_group_code_list')


class Group_codeCreateView(Group_codeView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_group_code_list')


class Group_codeDateDetailView(Group_codeDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_group_code_list')


class Group_codeDayArchiveView(
    Group_codeDateView, Group_codeBaseListView, DayArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_group_code_list')


class Group_codeDeleteView(Group_codeView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_group_code_list')


class Group_codeDetailView(Group_codeView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_group_code_list')


class Group_codeListView(Group_codeBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_group_code_list')


class Group_codeMonthArchiveView(
    Group_codeDateView, Group_codeBaseListView, MonthArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_group_code_list')


class Group_codeTodayArchiveView(
    Group_codeDateView, Group_codeBaseListView, TodayArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_group_code_list')


class Group_codeUpdateView(Group_codeView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_group_code_list')


class Group_codeWeekArchiveView(
    Group_codeDateView, Group_codeBaseListView, WeekArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_group_code_list')


class Group_codeYearArchiveView(
    Group_codeDateView, Group_codeBaseListView, YearArchiveView):
    make_object_list = True



