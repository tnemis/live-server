from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Religion
from django.contrib import auth, messages


class ReligionView(object):
    model = Religion

    def get_template_names(self):
        """Nest templates within religion directory."""
        tpl = super(ReligionView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'religion'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ReligionBaseListView(ReligionView):
    paginate_by = 10



class ReligionCreateView(ReligionView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_religion_list')




class ReligionDeleteView(ReligionView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_religion_list')


class ReligionDetailView(ReligionView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_religion_list')


class ReligionListView(ReligionBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_religion_list')




class ReligionUpdateView(ReligionView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_religion_list')





