from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView


from school.models import School_category


class School_categoryView(object):
    model = School_category

    def get_template_names(self):
        """Nest templates within school_category directory."""
        tpl = super(School_categoryView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'school_category'
        #self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        self.template_name = tpl[:7]+'school_category/'+tpl[7:]
        return [self.template_name]


class School_categoryBaseListView(School_categoryView):
    paginate_by = 10

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_category_list')



class School_categoryCreateView(School_categoryView, CreateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_category_list')




class School_categoryDeleteView(School_categoryView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_category_list')


class School_categoryDetailView(School_categoryView, DetailView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_category_list')


class School_categoryListView(School_categoryBaseListView, ListView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_category_list')




class School_categoryUpdateView(School_categoryView, UpdateView):
    pass

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('school_school_category_list')





