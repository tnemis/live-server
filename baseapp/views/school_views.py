from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from baseapp.models import School
from django.contrib import auth, messages


class SchoolView(object):
    model = School

    def get_template_names(self):
        """Nest templates within school directory."""
        tpl = super(SchoolView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class SchoolBaseListView(SchoolView):
    paginate_by = 10



class SchoolCreateView(SchoolView, CreateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        messages.add_message(
                self.request,
                messages.SUCCESS,"Successfully created."
            )
        return reverse('baseapp_school_list')




class SchoolDeleteView(SchoolView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_school_list')


class SchoolDetailView(SchoolView, DetailView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_school_list')


class SchoolListView(SchoolBaseListView, ListView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_school_list')




class SchoolUpdateView(SchoolView, UpdateView):
    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('baseapp_school_list')





