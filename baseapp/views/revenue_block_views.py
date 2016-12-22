from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Revenue_block


class Revenue_blockView(object):
    model = Revenue_block

    def get_template_names(self):
        """Nest templates within revenue_block directory."""
        tpl = super(Revenue_blockView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'revenue_block'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class Revenue_blockBaseListView(Revenue_blockView):
    paginate_by = 10



class Revenue_blockCreateView(Revenue_blockView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_revenue_block_list')




class Revenue_blockDeleteView(Revenue_blockView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_revenue_block_list')


class Revenue_blockDetailView(Revenue_blockView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_revenue_block_list')


class Revenue_blockListView(Revenue_blockBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_revenue_block_list')




class Revenue_blockUpdateView(Revenue_blockView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_revenue_block_list')





