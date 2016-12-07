from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Schemes
from django.contrib import auth, messages


class SchemesView(object):
    model = Schemes

    def get_template_names(self):
        """Nest templates within schemes directory."""
        tpl = super(SchemesView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'schemes'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class SchemesBaseListView(SchemesView):
    paginate_by = 10



class SchemesCreateView(SchemesView, CreateView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_schemes_list')





class SchemesDeleteView(SchemesView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_schemes_list')


class SchemesDetailView(SchemesView, DetailView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_schemes_list')



class SchemesListView(SchemesBaseListView, ListView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_schemes_list')





class SchemesUpdateView(SchemesView, UpdateView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_schemes_list')






