from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Management
from django.contrib import auth, messages


class ManagementView(object):
    model = Management

    def get_template_names(self):
        """Nest templates within management directory."""
        tpl = super(ManagementView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'management'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class ManagementBaseListView(ManagementView):
    paginate_by = 10



class ManagementCreateView(ManagementView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_management_list')




class ManagementDeleteView(ManagementView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_management_list')


class ManagementDetailView(ManagementView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_management_list')


class ManagementListView(ManagementBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_management_list')




class ManagementUpdateView(ManagementView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_management_list')





