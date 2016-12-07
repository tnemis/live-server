from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Assembly


class AssemblyView(object):
    model = Assembly

    def get_template_names(self):
        """Nest templates within assembly directory."""
        tpl = super(AssemblyView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'assembly'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class AssemblyBaseListView(AssemblyView):
    paginate_by = 10



class AssemblyCreateView(AssemblyView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_assembly_list')




class AssemblyDeleteView(AssemblyView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_assembly_list')


class AssemblyDetailView(AssemblyView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_assembly_list')


class AssemblyListView(AssemblyBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_assembly_list')




class AssemblyUpdateView(AssemblyView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_assembly_list')





