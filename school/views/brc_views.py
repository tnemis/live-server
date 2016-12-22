from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from school.models import Brc


class BrcView(object):
    model = Brc

    def get_template_names(self):
        """Nest templates within brc directory."""
        tpl = super(BrcView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'brc'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class BrcBaseListView(BrcView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_brc_list')



class BrcCreateView(BrcView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_brc_list')




class BrcDeleteView(BrcView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_brc_list')


class BrcDetailView(BrcView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_brc_list')


class BrcListView(BrcBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_brc_list')




class BrcUpdateView(BrcView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_brc_list')





