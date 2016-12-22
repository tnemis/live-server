from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_loan


class Teacher_loanView(object):
    model = Teacher_loan

    def get_template_names(self):
        """Nest templates within teacher_loan directory."""
        tpl = super(Teacher_loanView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_loan'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_loan/'+tpl[8:]
        return [self.template_name]


class Teacher_loanDateView(Teacher_loanView):
    date_field = 'timestamp'
    month_format = '%m'

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanBaseListView(Teacher_loanView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanArchiveIndexView(
    Teacher_loanDateView, Teacher_loanBaseListView, ArchiveIndexView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanCreateView(Teacher_loanView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanDateDetailView(Teacher_loanDateView, DateDetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanDayArchiveView(
    Teacher_loanDateView, Teacher_loanBaseListView, DayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanDeleteView(Teacher_loanView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanDetailView(Teacher_loanView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanListView(Teacher_loanBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanMonthArchiveView(
    Teacher_loanDateView, Teacher_loanBaseListView, MonthArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanTodayArchiveView(
    Teacher_loanDateView, Teacher_loanBaseListView, TodayArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanUpdateView(Teacher_loanView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanWeekArchiveView(
    Teacher_loanDateView, Teacher_loanBaseListView, WeekArchiveView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')


class Teacher_loanYearArchiveView(
    Teacher_loanDateView, Teacher_loanBaseListView, YearArchiveView):
    make_object_list = True

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_loan_list')



