from __future__ import unicode_literals

from django.conf.urls import patterns, url
from emis_account.views import home
from emis_account.views import register_import
from emis_account.views import student_count_update, photo_update, generate_unique_id
from emis_account.views import SignupView, LoginView, LogoutView, DeleteView
from emis_account.views import ConfirmEmailView
from emis_account.views import ChangePasswordView, PasswordResetView, PasswordResetTokenView
from emis_account.views import SettingsView
from django.contrib.auth.views import login
# from cerberos.decorators import watch_logins


urlpatterns = patterns("",
	url(r'^$', home),
    url(r'^register_import/$', register_import),
    url(r'^student_count_update/$', student_count_update),
    url(r'^generate_unique_id/$', generate_unique_id),
    url(r'^photo_update/$', photo_update),
    url(r"^signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^login/$", LoginView.as_view(), name="account_login"),
    url(r"^logout/$", LogoutView.as_view(), name="account_logout"),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password"),
    url(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings"),
    #url(r"^delete/$", DeleteView.as_view(), name="account_delete"),

    # url(r'^tnschools_mail/$', tnschools_mail),

)
