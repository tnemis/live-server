from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Community
from django.contrib import auth, messages


class CommunityView(object):
    model = Community

    def get_template_names(self):
        """Nest templates within community directory."""
        tpl = super(CommunityView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'community'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class CommunityBaseListView(CommunityView):
    paginate_by = 10



class CommunityCreateView(CommunityView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_community_list')




class CommunityDeleteView(CommunityView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_community_list')


class CommunityDetailView(CommunityView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_community_list')


class CommunityListView(CommunityBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_community_list')




class CommunityUpdateView(CommunityView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_community_list')





