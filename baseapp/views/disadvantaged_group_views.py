from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Disadvantaged_group
from django.contrib import auth, messages


class Disadvantaged_groupView(object):
    model = Disadvantaged_group

    def get_template_names(self):
        """Nest templates within disadvantaged_group directory."""
        tpl = super(Disadvantaged_groupView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'disadvantaged_group'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Disadvantaged_groupBaseListView(Disadvantaged_groupView):
    paginate_by = 10



class Disadvantaged_groupCreateView(Disadvantaged_groupView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_disadvantaged_group_list')




class Disadvantaged_groupDeleteView(Disadvantaged_groupView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_disadvantaged_group_list')


class Disadvantaged_groupDetailView(Disadvantaged_groupView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_disadvantaged_group_list')


class Disadvantaged_groupListView(Disadvantaged_groupBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_disadvantaged_group_list')




class Disadvantaged_groupUpdateView(Disadvantaged_groupView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_disadvantaged_group_list')





