from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_professional


class Teacher_professionalView(object):
    model = Teacher_professional

    def get_template_names(self):
        """Nest templates within teacher_professional directory."""
        tpl = super(Teacher_professionalView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_professional'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_professional/'+tpl[8:]
        return [self.template_name]


class Teacher_professionalDateView(Teacher_professionalView):
    date_field = 'timestamp'
    month_format = '%m'


class Teacher_professionalBaseListView(Teacher_professionalView):
    paginate_by = 10


class Teacher_professionalArchiveIndexView(
    Teacher_professionalDateView, Teacher_professionalBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalCreateView(Teacher_professionalView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalDateDetailView(Teacher_professionalDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalDayArchiveView(
    Teacher_professionalDateView, Teacher_professionalBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalDeleteView(Teacher_professionalView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')


class Teacher_professionalDetailView(Teacher_professionalView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalListView(Teacher_professionalBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalMonthArchiveView(
    Teacher_professionalDateView, Teacher_professionalBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalTodayArchiveView(
    Teacher_professionalDateView, Teacher_professionalBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalUpdateView(Teacher_professionalView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalWeekArchiveView(
    Teacher_professionalDateView, Teacher_professionalBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')



class Teacher_professionalYearArchiveView(
    Teacher_professionalDateView, Teacher_professionalBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_professional_list')




