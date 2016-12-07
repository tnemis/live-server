from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_immovalble_property


class Teacher_immovalble_propertyView(object):
    model = Teacher_immovalble_property

    def get_template_names(self):
        """Nest templates within teacher_immovalble_property directory."""
        tpl = super(Teacher_immovalble_propertyView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_immovalble_property'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_immovalble_property/'+tpl[8:]
        return [self.template_name]


class Teacher_immovalble_propertyDateView(Teacher_immovalble_propertyView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyBaseListView(Teacher_immovalble_propertyView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyArchiveIndexView(
    Teacher_immovalble_propertyDateView, Teacher_immovalble_propertyBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyCreateView(Teacher_immovalble_propertyView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyDateDetailView(Teacher_immovalble_propertyDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyDayArchiveView(
    Teacher_immovalble_propertyDateView, Teacher_immovalble_propertyBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyDeleteView(Teacher_immovalble_propertyView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyDetailView(Teacher_immovalble_propertyView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyListView(Teacher_immovalble_propertyBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyMonthArchiveView(
    Teacher_immovalble_propertyDateView, Teacher_immovalble_propertyBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyTodayArchiveView(
    Teacher_immovalble_propertyDateView, Teacher_immovalble_propertyBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyUpdateView(Teacher_immovalble_propertyView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyWeekArchiveView(
    Teacher_immovalble_propertyDateView, Teacher_immovalble_propertyBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')


class Teacher_immovalble_propertyYearArchiveView(
    Teacher_immovalble_propertyDateView, Teacher_immovalble_propertyBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_immovalble_property_list')



