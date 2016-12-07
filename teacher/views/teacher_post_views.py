from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from teacher.models import Teacher_post


class Teacher_postView(object):
    model = Teacher_post

    def get_template_names(self):
        """Nest templates within teacher_post directory."""
        tpl = super(Teacher_postView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'teacher_post'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:8]+'teacher_post/'+tpl[8:]
        return [self.template_name]


class Teacher_postDateView(Teacher_postView):
    date_field = 'timestamp'
    month_format = '%m'


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postBaseListView(Teacher_postView):
    paginate_by = 10


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postArchiveIndexView(
    Teacher_postDateView, Teacher_postBaseListView, ArchiveIndexView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postCreateView(Teacher_postView, CreateView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postDateDetailView(Teacher_postDateView, DateDetailView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postDayArchiveView(
    Teacher_postDateView, Teacher_postBaseListView, DayArchiveView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postDeleteView(Teacher_postView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postDetailView(Teacher_postView, DetailView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postListView(Teacher_postBaseListView, ListView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postMonthArchiveView(
    Teacher_postDateView, Teacher_postBaseListView, MonthArchiveView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postTodayArchiveView(
    Teacher_postDateView, Teacher_postBaseListView, TodayArchiveView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postUpdateView(Teacher_postView, UpdateView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postWeekArchiveView(
    Teacher_postDateView, Teacher_postBaseListView, WeekArchiveView):
    pass


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')


class Teacher_postYearArchiveView(
    Teacher_postDateView, Teacher_postBaseListView, YearArchiveView):
    make_object_list = True


    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teacher_teacher_post_list')



