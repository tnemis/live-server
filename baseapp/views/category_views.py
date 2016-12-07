from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import Category
from django.contrib import auth, messages


class CategoryView(object):
    model = Category

    def get_template_names(self):
        """Nest templates within category directory."""
        tpl = super(CategoryView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'category'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class CategoryBaseListView(CategoryView):
    paginate_by = 10



class CategoryCreateView(CategoryView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_category_list')




class CategoryDeleteView(CategoryView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_category_list')


class CategoryDetailView(CategoryView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_category_list')


class CategoryListView(CategoryBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_category_list')




class CategoryUpdateView(CategoryView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_category_list')





