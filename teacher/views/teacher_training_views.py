from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_training


class Teacher_trainingView(object):
    model = Teacher_training

    def get_template_names(self):
        """Nest templates within teacher_training directory."""
        tpl = super(Teacher_trainingView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_training'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_training/'+tpl[8:]
        return [self.template_name]


class Teacher_trainingDateView(Teacher_trainingView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingBaseListView(Teacher_trainingView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingArchiveIndexView(
    Teacher_trainingDateView, Teacher_trainingBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingCreateView(Teacher_trainingView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingDateDetailView(Teacher_trainingDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingDayArchiveView(
    Teacher_trainingDateView, Teacher_trainingBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingDeleteView(Teacher_trainingView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingDetailView(Teacher_trainingView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingListView(Teacher_trainingBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingMonthArchiveView(
    Teacher_trainingDateView, Teacher_trainingBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingTodayArchiveView(
    Teacher_trainingDateView, Teacher_trainingBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingUpdateView(Teacher_trainingView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingWeekArchiveView(
    Teacher_trainingDateView, Teacher_trainingBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')


class Teacher_trainingYearArchiveView(
    Teacher_trainingDateView, Teacher_trainingBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_training_list')



