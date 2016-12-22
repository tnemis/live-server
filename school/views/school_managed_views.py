from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from school.models import School_managed


class School_managedView(object):
    model = School_managed

    def get_template_names(self):
        """Nest templates within school_managed directory."""
        #import ipdb; ipdb.set_trace()
        tpl = super(School_managedView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_managed'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_managed/'+tpl[7:]
        return [self.template_name]


class School_managedBaseListView(School_managedView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_managed_list')



class School_managedCreateView(School_managedView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_managed_list')




class School_managedDeleteView(School_managedView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_managed_list')


class School_managedDetailView(School_managedView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_managed_list')


class School_managedListView(School_managedBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_managed_list')




class School_managedUpdateView(School_managedView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_managed_list')





