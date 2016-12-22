from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_movable_property


class Teacher_movable_propertyView(object):
    model = Teacher_movable_property

    def get_template_names(self):
        """Nest templates within teacher_movable_property directory."""
        tpl = super(Teacher_movable_propertyView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_movable_property'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_movable_property/'+tpl[8:]
        return [self.template_name]


class Teacher_movable_propertyDateView(Teacher_movable_propertyView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyBaseListView(Teacher_movable_propertyView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyArchiveIndexView(
    Teacher_movable_propertyDateView, Teacher_movable_propertyBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyCreateView(Teacher_movable_propertyView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyDateDetailView(Teacher_movable_propertyDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyDayArchiveView(
    Teacher_movable_propertyDateView, Teacher_movable_propertyBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyDeleteView(Teacher_movable_propertyView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyDetailView(Teacher_movable_propertyView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyListView(Teacher_movable_propertyBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyMonthArchiveView(
    Teacher_movable_propertyDateView, Teacher_movable_propertyBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyTodayArchiveView(
    Teacher_movable_propertyDateView, Teacher_movable_propertyBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyUpdateView(Teacher_movable_propertyView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyWeekArchiveView(
    Teacher_movable_propertyDateView, Teacher_movable_propertyBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')


class Teacher_movable_propertyYearArchiveView(
    Teacher_movable_propertyDateView, Teacher_movable_propertyBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_movable_property_list')



