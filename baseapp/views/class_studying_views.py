from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from baseapp.models import Class_Studying
from django.contrib import auth, messages


class Class_StudyingView(object):
    model = Class_Studying

    def get_template_names(self):
        """Nest templates within class_studying directory."""
        tpl = super(Class_StudyingView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'class_studying'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Class_StudyingDateView(Class_StudyingView):
    date_field = 'created_date'
    month_format = '%m'


class Class_StudyingBaseListView(Class_StudyingView):
    paginate_by = 10


class Class_StudyingArchiveIndexView(
    Class_StudyingDateView, Class_StudyingBaseListView, ArchiveIndexView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_class_studying_list')



class Class_StudyingCreateView(Class_StudyingView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_class_studying_list')



class Class_StudyingDateDetailView(Class_StudyingDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_class_studying_list')



class Class_StudyingDayArchiveView(
    Class_StudyingDateView, Class_StudyingBaseListView, DayArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_class_studying_list')



class Class_StudyingDeleteView(Class_StudyingView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_class_studying_list')


class Class_StudyingDetailView(Class_StudyingView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_class_studying_list')



class Class_StudyingListView(Class_StudyingBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_class_studying_list')



class Class_StudyingMonthArchiveView(
    Class_StudyingDateView, Class_StudyingBaseListView, MonthArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_class_studying_list')



class Class_StudyingTodayArchiveView(
    Class_StudyingDateView, Class_StudyingBaseListView, TodayArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_class_studying_list')



class Class_StudyingUpdateView(Class_StudyingView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_class_studying_list')



class Class_StudyingWeekArchiveView(
    Class_StudyingDateView, Class_StudyingBaseListView, WeekArchiveView):
        def get_success_url(self):
            from django.core.urlresolvers import reverse
            return reverse('baseapp_class_studying_list')


class Class_StudyingYearArchiveView(
    Class_StudyingDateView, Class_StudyingBaseListView, YearArchiveView):
    make_object_list = True



