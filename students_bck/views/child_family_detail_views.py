from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from students.models import Child_family_detail


class Child_family_detailView(object):
    model = Child_family_detail

    def get_template_names(self):
        """Nest templates within child_family_detail directory."""
        tpl = super(Child_family_detailView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'child_family_detail'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Child_family_detailDateView(Child_family_detailView):
    date_field = 'created_date'
    month_format = '%m'


class Child_family_detailBaseListView(Child_family_detailView):
    paginate_by = 10


class Child_family_detailArchiveIndexView(
    Child_family_detailDateView, Child_family_detailBaseListView, ArchiveIndexView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailCreateView(Child_family_detailView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailDateDetailView(Child_family_detailDateView, DateDetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailDayArchiveView(
    Child_family_detailDateView, Child_family_detailBaseListView, DayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailDeleteView(Child_family_detailView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')


class Child_family_detailDetailView(Child_family_detailView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailListView(Child_family_detailBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailMonthArchiveView(
    Child_family_detailDateView, Child_family_detailBaseListView, MonthArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailTodayArchiveView(
    Child_family_detailDateView, Child_family_detailBaseListView, TodayArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailUpdateView(Child_family_detailView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailWeekArchiveView(
    Child_family_detailDateView, Child_family_detailBaseListView, WeekArchiveView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('students_child_family_detail_list')



class Child_family_detailYearArchiveView(
    Child_family_detailDateView, Child_family_detailBaseListView, YearArchiveView):
    make_object_list = True



