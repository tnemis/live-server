from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from school.models import School_type


class School_typeView(object):
    model = School_type

    def get_template_names(self):
        """Nest templates within school_type directory."""
        tpl = super(School_typeView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_type'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_type/'+tpl[7:]
        return [self.template_name]


class School_typeBaseListView(School_typeView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_type_list')



class School_typeCreateView(School_typeView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_type_list')




class School_typeDeleteView(School_typeView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_type_list')


class School_typeDetailView(School_typeView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_type_list')


class School_typeListView(School_typeBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_type_list')




class School_typeUpdateView(School_typeView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_type_list')





