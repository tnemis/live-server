from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Block
from django.contrib import auth, messages


class BlockView(object):
    model = Block

    def get_template_names(self):
        """Nest templates within block directory."""
        tpl = super(BlockView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'block'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class BlockBaseListView(BlockView):
    paginate_by = 75



class BlockCreateView(BlockView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_block_list')




class BlockDeleteView(BlockView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_block_list')


class BlockDetailView(BlockView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_block_list')


class BlockListView(BlockBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_block_list')




class BlockUpdateView(BlockView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_block_list')





