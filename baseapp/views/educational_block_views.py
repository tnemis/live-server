from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Educational_block


class Educational_blockView(object):
    model = Educational_block

    def get_template_names(self):
        """Nest templates within educational_block directory."""
        tpl = super(Educational_blockView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'educational_block'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Educational_blockBaseListView(Educational_blockView):
    paginate_by = 10



class Educational_blockCreateView(Educational_blockView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_block_list')




class Educational_blockDeleteView(Educational_blockView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_block_list')


class Educational_blockDetailView(Educational_blockView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_block_list')


class Educational_blockListView(Educational_blockBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_block_list')




class Educational_blockUpdateView(Educational_blockView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_educational_block_list')





