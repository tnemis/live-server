from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from school.models import School_recognition


class School_recognitionView(object):
    model = School_recognition

    def get_template_names(self):
        """Nest templates within school_recognition directory."""
        tpl = super(School_recognitionView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_recognition'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_recognition/'+tpl[7:]
        return [self.template_name]


class School_recognitionDateView(School_recognitionView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionBaseListView(School_recognitionView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionArchiveIndexView(
    School_recognitionDateView, School_recognitionBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionCreateView(School_recognitionView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionDateDetailView(School_recognitionDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionDayArchiveView(
    School_recognitionDateView, School_recognitionBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionDeleteView(School_recognitionView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionDetailView(School_recognitionView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionListView(School_recognitionBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionMonthArchiveView(
    School_recognitionDateView, School_recognitionBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionTodayArchiveView(
    School_recognitionDateView, School_recognitionBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionUpdateView(School_recognitionView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionWeekArchiveView(
    School_recognitionDateView, School_recognitionBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')


class School_recognitionYearArchiveView(
    School_recognitionDateView, School_recognitionBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_recognition_list')



