from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin,SuperuserRequiredMixin,LoginRequiredMixin
from django.views.generic import TemplateView

class ContactList(LoginRequiredMixin,SuperuserRequiredMixin,TemplateView):
	login_url = '/accounts/login/'
	redirect_field_name = 'next'
	raise_exception = True
	template_name = "homepage.html"
    

		

    