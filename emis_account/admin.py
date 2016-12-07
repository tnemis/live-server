from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from emis_account.models import Account, SignupCode, AccountDeletion, EmailAddress
from emis_account.models import User_Category

class SignupCodeAdmin(admin.ModelAdmin):

    list_display = ["code", "max_uses", "use_count", "expiry", "created"]
    search_fields = ["code", "email"]
    list_filter = ["created"]

class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "verified", "primary"]
    search_fields = ["user", "email"]
    list_filter = ["user"]

#admin.site.unregister(User)
admin.site.register(Account)
class MyAuthAdmin(admin.ModelAdmin):
	exclude = ["email", "firstname", "lastname"]
	search_fields = ["username"]
	list_filter = ["username"]
#admin.site.register(User,MyAuthAdmin)
#admin.site.register(SignupCode, SignupCodeAdmin)
#admin.site.register(AccountDeletion, list_display=["email", "date_requested", "date_expunged"])
admin.site.register(EmailAddress, EmailAddressAdmin)
admin.site.register(User_Category)
