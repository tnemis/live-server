from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from school.models import Area_classification


class Area_classificationView(object):
    model = Area_classification

    def get_template_names(self):
        """Nest templates within area_classification directory."""
        tpl = super(Area_classificationView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'area_classification'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Area_classificationBaseListView(Area_classificationView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_area_classification_list')



class Area_classificationCreateView(Area_classificationView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_area_classification_list')




class Area_classificationDeleteView(Area_classificationView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_area_classification_list')


class Area_classificationDetailView(Area_classificationView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_area_classification_list')


class Area_classificationListView(Area_classificationBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_area_classification_list')




class Area_classificationUpdateView(Area_classificationView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_area_classification_list')





