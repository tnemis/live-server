from django.contrib import admin
from students.models import Child_detail
class ChildAdmin(admin.ModelAdmin):
	


    def queryset(self, request):
        """
        Filter the Child objects  to only
        display those for the currently signed in user.
        """
        qs = super(ChildAdmin, self).queryset(request)
        if request.user.is_superuser:
        	return qs
        if request.user.user_category == 'block':
        	return qs.filter(block=request.user.account.associated_with)
        if request.user.user_category == 'school':
        	return qs.filter(school=request.user.account.associated_with)
        if request.user.user_category == 'district':
        	return qs.filter(district=request.user.account.associated_with)
        # Register your models here.

admin.site.register(Child_detail,ChildAdmin)
