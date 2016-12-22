from __future__ import unicode_literals

from emis_account.conf import settings
from emis_account.utils import handle_redirect_to_login


class LoginRequiredMixin(object):

    redirect_field_name = "next"
    login_url = None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        if request.user.is_authenticated():
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
        return self.redirect_to_login()

    def get_login_url(self):
        return self.login_url or settings.ACCOUNT_LOGIN_URL

    def get_next_url(self):
        return self.request.get_full_path()

    def redirect_to_login(self):
        return handle_redirect_to_login(
            self.request,
            redirect_field_name=self.redirect_field_name,
            login_url=self.get_login_url(),
            next_url=self.get_next_url(),
        )
