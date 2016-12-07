from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Habitation
from django.contrib import auth, messages


class HabitationView(object):
    model = Habitation

    def get_template_names(self):
        """Nest templates within habitation directory."""
        tpl = super(HabitationView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'habitation'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class HabitationBaseListView(HabitationView):
    paginate_by = 10



class HabitationCreateView(HabitationView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_habitation_list')




class HabitationDeleteView(HabitationView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_habitation_list')


class HabitationDetailView(HabitationView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_habitation_list')


class HabitationListView(HabitationBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_habitation_list')




class HabitationUpdateView(HabitationView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_habitation_list')





