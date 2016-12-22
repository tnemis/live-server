from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Taluk


class TalukView(object):
    model = Taluk

    def get_template_names(self):
        """Nest templates within taluk directory."""
        tpl = super(TalukView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'taluk'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class TalukBaseListView(TalukView):
    paginate_by = 10



class TalukCreateView(TalukView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_taluk_list')




class TalukDeleteView(TalukView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_taluk_list')


class TalukDetailView(TalukView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_taluk_list')
        


class TalukListView(TalukBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_taluk_list')
        




class TalukUpdateView(TalukView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_taluk_list')
        





