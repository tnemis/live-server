from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Differently_abled
from django.contrib import auth, messages


class Differently_abledView(object):
    model = Differently_abled

    def get_template_names(self):
        """Nest templates within differently_abled directory."""
        tpl = super(Differently_abledView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'differently_abled'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Differently_abledBaseListView(Differently_abledView):
    paginate_by = 10



class Differently_abledCreateView(Differently_abledView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_differently_abled_list')




class Differently_abledDeleteView(Differently_abledView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_differently_abled_list')


class Differently_abledDetailView(Differently_abledView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_differently_abled_list')


class Differently_abledListView(Differently_abledBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_differently_abled_list')




class Differently_abledUpdateView(Differently_abledView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_differently_abled_list')





