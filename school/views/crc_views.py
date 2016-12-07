from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from school.models import Crc


class CrcView(object):
    model = Crc

    def get_template_names(self):
        """Nest templates within crc directory."""
        tpl = super(CrcView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'crc'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class CrcBaseListView(CrcView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_crc_list')



class CrcCreateView(CrcView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_crc_list')




class CrcDeleteView(CrcView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_crc_list')


class CrcDetailView(CrcView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_crc_list')


class CrcListView(CrcBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_crc_list')




class CrcUpdateView(CrcView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_crc_list')





