from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Language
from django.contrib import auth, messages


class LanguageView(object):
    model = Language

    def get_template_names(self):
        """Nest templates within language directory."""
        tpl = super(LanguageView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'language'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class LanguageBaseListView(LanguageView):
    paginate_by = 10



class LanguageCreateView(LanguageView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_language_list')




class LanguageDeleteView(LanguageView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_language_list')


class LanguageDetailView(LanguageView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_language_list')


class LanguageListView(LanguageBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_language_list')




class LanguageUpdateView(LanguageView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_language_list')





