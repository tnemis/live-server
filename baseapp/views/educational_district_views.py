from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Educational_district


class Educational_districtView(object):
    model = Educational_district

    def get_template_names(self):
        """Nest templates within educational_district directory."""
        tpl = super(Educational_districtView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'educational_district'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Educational_districtBaseListView(Educational_districtView):
    paginate_by = 10



class Educational_districtCreateView(Educational_districtView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_district_list')




class Educational_districtDeleteView(Educational_districtView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_district_list')


class Educational_districtDetailView(Educational_districtView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_district_list')


class Educational_districtListView(Educational_districtBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_district_list')




class Educational_districtUpdateView(Educational_districtView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_district_list')





