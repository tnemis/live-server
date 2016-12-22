from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView
from django.core.urlresolvers import reverse

from baseapp.models import District
from django.contrib import auth, messages


class DistrictView(object):
    model = District

    def get_template_names(self):
        """Nest templates within district directory."""
        tpl = super(DistrictView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'district'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class DistrictBaseListView(DistrictView):
    paginate_by = 10



class DistrictCreateView(DistrictView, CreateView):
    def get_success_url(self):
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_district_list')



class DistrictDeleteView(DistrictView, DeleteView):

    def get_success_url(self):

        return reverse('baseapp_district_list')


class DistrictDetailView(DistrictView, DetailView):
    
    def get_success_url(self):

        return reverse('baseapp_district_list')


class DistrictListView(DistrictBaseListView, ListView):
    def get_success_url(self):

        return reverse('baseapp_district_list')



class DistrictUpdateView(DistrictView, UpdateView):
    def get_success_url(self):

        return reverse('baseapp_district_list')





