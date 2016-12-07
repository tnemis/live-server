from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Parliamentary


class ParliamentaryView(object):
    model = Parliamentary

    def get_template_names(self):
        """Nest templates within parliamentary directory."""
        tpl = super(ParliamentaryView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'parliamentary'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ParliamentaryBaseListView(ParliamentaryView):
    paginate_by = 10



class ParliamentaryCreateView(ParliamentaryView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_parliamentary_list')




class ParliamentaryDeleteView(ParliamentaryView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_parliamentary_list')


class ParliamentaryDetailView(ParliamentaryView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_parliamentary_list')


class ParliamentaryListView(ParliamentaryBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_parliamentary_list')




class ParliamentaryUpdateView(ParliamentaryView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_parliamentary_list')





