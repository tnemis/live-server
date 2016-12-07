from __future__ import unicode_literals

from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormView

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.sites.models import get_current_site
from django.contrib.auth.tokens import default_token_generator

from emis_account import signals
from emis_account.compat import get_user_model
from emis_account.conf import settings
from emis_account.forms import SignupForm, LoginUsernameForm
from emis_account.forms import ChangePasswordForm, PasswordResetForm, PasswordResetTokenForm
from emis_account.forms import SettingsForm
from emis_account.hooks import hookset
from emis_account.mixins import LoginRequiredMixin
from emis_account.models import SignupCode, EmailAddress, EmailConfirmation, Account, AccountDeletion
from emis_account.utils import default_redirect
from django.shortcuts import render
from django.contrib.auth.models import Group , User
import csv
from emis_account.models import Account
from students.models import Child_detail, School_child_count
from baseapp.models import District, Block, School, Habitation, Zone
def home(request):
    return render(request,"homepage.html")


class SignupView(FormView):

    template_name = "account/signup.html"
    template_name_ajax = "account/ajax/signup.html"
    template_name_email_confirmation_sent = "account/email_confirmation_sent.html"
    template_name_email_confirmation_sent_ajax = "account/ajax/email_confirmation_sent.html"
    template_name_signup_closed = "account/signup_closed.html"
    template_name_signup_closed_ajax = "account/ajax/signup_closed.html"
    form_class = SignupForm
    form_kwargs = {}
    redirect_field_name = "next"
    messages = {
        "email_confirmation_sent": {
            "level": messages.INFO,
            "text": _("Confirmation email sent to {email}.")
        },
        "invalid_signup_code": {
            "level": messages.WARNING,
            "text": _("The code {code} is invalid.")
        }
    }

    def __init__(self, *args, **kwargs):
        self.created_user = None
        kwargs["signup_code"] = None
        super(SignupView, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(default_redirect(self.request, settings.ACCOUNT_LOGIN_REDIRECT_URL))
        if not self.is_open():
            return self.closed()
        return super(SignupView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if not self.is_open():
            return self.closed()
        return super(SignupView, self).post(*args, **kwargs)

    def get_initial(self):
        initial = super(SignupView, self).get_initial()
        if self.signup_code:
            initial["code"] = self.signup_code.code
            if self.signup_code.email:
                initial["email"] = self.signup_code.email
        return initial

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.template_name_ajax]
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def get_form_kwargs(self):
        kwargs = super(SignupView, self).get_form_kwargs()
        kwargs.update(self.form_kwargs)
        return kwargs

    def form_invalid(self, form):
        signals.user_sign_up_attempt.send(
            sender=SignupForm,
            username=form.data.get("username"),
            email=form.data.get("email"),
            result=form.is_valid()
        )
        return super(SignupView, self).form_invalid(form)

    def form_valid(self, form):
        self.created_user = self.create_user(form, commit=False)

        # prevent User post_save signal from creating an Account instance
        # we want to handle that ourself.
        self.created_user._disable_account_creation = True
        self.created_user.save()
        #adding group to the users created
        if str(form.cleaned_data.get("category").user_category) == 'school':
            g = Group.objects.get(name='school')
            g.user_set.add(self.created_user)
            g = Group.objects.get(name='students')
            g.user_set.add(self.created_user)

        email_address = self.create_email_address(form)
        if settings.ACCOUNT_EMAIL_CONFIRMATION_REQUIRED and not email_address.verified:
            self.created_user.is_active = False
            self.created_user.save()
        self.create_account(form)
        self.after_signup(form)
        if settings.ACCOUNT_EMAIL_CONFIRMATION_EMAIL and not email_address.verified:
            self.send_email_confirmation(email_address)
        if settings.ACCOUNT_EMAIL_CONFIRMATION_REQUIRED and not email_address.verified:
            return self.email_confirmation_required_response()
        else:
            show_message = [
                settings.ACCOUNT_EMAIL_CONFIRMATION_EMAIL,
                self.messages.get("email_confirmation_sent"),
                not email_address.verified
            ]
            if all(show_message):
                messages.add_message(
                    self.request,
                    self.messages["email_confirmation_sent"]["level"],
                    self.messages["email_confirmation_sent"]["text"].format(**{
                        "email": form.cleaned_data["email"]
                    })
                )
            self.login_user()
        return redirect(self.get_success_url())

    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_SIGNUP_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def create_user(self, form, commit=True, **kwargs):
        user = get_user_model()(**kwargs)
        username = form.cleaned_data.get("username")
        if username is None:
            username = self.generate_username(form)
        user.username = username
        user.email = form.cleaned_data["email"].strip()
        password = form.cleaned_data.get("password")

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        

       

        if commit:
            user.save()
        
        return user

    def create_account(self, form):
        add_account = Account (
            user = self.created_user,
            mobile_number = form.cleaned_data.get('mobile_number'),
            user_category = form.cleaned_data.get('category'),
            associated_with = form.cleaned_data.get('associated'),


            )

        add_account.save()
        return Account.create(request=self.request, user=self.created_user, create_email=False)

    def generate_username(self, form):
        raise NotImplementedError("Unable to generate username by default. "
            "Override SignupView.generate_username in a subclass.")

    def create_email_address(self, form, **kwargs):
        kwargs.setdefault("primary", True)
        kwargs.setdefault("verified", False)
        if self.signup_code:
            self.signup_code.use(self.created_user)
            kwargs["verified"] = self.signup_code.email and self.created_user.email == self.signup_code.email
        return EmailAddress.objects.add_email(self.created_user, self.created_user.email, **kwargs)

    def send_email_confirmation(self, email_address):
        email_address.send_confirmation(site=get_current_site(self.request))

    def after_signup(self, form):
        signals.user_signed_up.send(sender=SignupForm, user=self.created_user, form=form)

    def login_user(self):
        # set backend on User object to bypass needing to call auth.authenticate
        self.created_user.backend = "django.contrib.auth.backends.ModelBackend"
        auth.login(self.request, self.created_user)
        self.request.session.set_expiry(0)

    def is_open(self):
        code = self.request.REQUEST.get("code")
        if code:
            try:
                self.signup_code = SignupCode.check(code)
            except SignupCode.InvalidCode:
                if self.messages.get("invalid_signup_code"):
                    messages.add_message(
                        self.request,
                        self.messages["invalid_signup_code"]["level"],
                        self.messages["invalid_signup_code"]["text"].format(**{
                            "code": code
                        })
                    )
                return settings.ACCOUNT_OPEN_SIGNUP
            else:
                return True
        else:
            return settings.ACCOUNT_OPEN_SIGNUP

    def email_confirmation_required_response(self):
        if self.request.is_ajax():
            template_name = self.template_name_email_confirmation_sent_ajax
        else:
            template_name = self.template_name_email_confirmation_sent
        response_kwargs = {
            "request": self.request,
            "template": template_name,
            "context": {
                "email": self.created_user.email,
                "success_url": self.get_success_url(),
            }
        }
        return self.response_class(**response_kwargs)

    def closed(self):
        if self.request.is_ajax():
            template_name = self.template_name_signup_closed_ajax
        else:
            template_name = self.template_name_signup_closed
        response_kwargs = {
            "request": self.request,
            "template": template_name,
        }
        return self.response_class(**response_kwargs)


class LoginView(FormView):

    template_name = "account/login.html"
    template_name_ajax = "account/ajax/login.html"
    form_class = LoginUsernameForm
    form_kwargs = {}
    redirect_field_name = "next"
   

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(LoginView, self).get(*args, **kwargs)

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.template_name_ajax]
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs.update(self.form_kwargs)
        return kwargs

    def form_invalid(self, form):
        signals.user_login_attempt.send(
            sender=LoginView,
            username=form.data.get(form.identifier_field),
            result=form.is_valid()
        )
        return super(LoginView, self).form_invalid(form)

    def form_valid(self, form):
        self.login_user(form)
        self.after_login(form)
        return redirect(self.get_success_url())

    def after_login(self, form):
        signals.user_logged_in.send(sender=LoginView, user=form.user, form=form)

    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_LOGIN_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def login_user(self, form):
        auth.login(self.request, form.user)
        expiry = settings.ACCOUNT_REMEMBER_ME_EXPIRY if form.cleaned_data.get("remember") else 0
        self.request.session.set_expiry(expiry)


class LogoutView(TemplateResponseMixin, View):

    template_name = "account/logout.html"
    redirect_field_name = "next"

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect(self.get_redirect_url())
        ctx = self.get_context_data()
        return self.render_to_response(ctx)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth.logout(self.request)
        return redirect(self.get_redirect_url())

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def get_redirect_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_LOGOUT_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)


class ConfirmEmailView(TemplateResponseMixin, View):

    htmethod_names = ["get", "post"]
    messages = {
        "email_confirmed": {
            "level": messages.SUCCESS,
            "text": _("You have confirmed {email}.")
        }
    }

    def get_template_names(self):
        return {
            "GET": ["account/email_confirm.html"],
            "POST": ["account/email_confirmed.html"],
        }[self.request.method]

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        ctx = self.get_context_data()
        return self.render_to_response(ctx)

    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm()
        self.after_confirmation(confirmation)
        redirect_url = self.get_redirect_url()
        if not redirect_url:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)
        if self.messages.get("email_confirmed"):
            messages.add_message(
                self.request,
                self.messages["email_confirmed"]["level"],
                self.messages["email_confirmed"]["text"].format(**{
                    "email": confirmation.email_address.email
                })
            )
        return redirect(redirect_url)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        try:
            return queryset.get(key=self.kwargs["key"].lower())
        except EmailConfirmation.DoesNotExist:
            raise Http404()

    def get_queryset(self):
        qs = EmailConfirmation.objects.all()
        qs = qs.select_related("email_address__user")
        return qs

    def get_context_data(self, **kwargs):
        ctx = kwargs
        ctx["confirmation"] = self.object
        return ctx

    def get_redirect_url(self):
        if self.request.user.is_authenticated():
            if not settings.ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL:
                return settings.ACCOUNT_LOGIN_REDIRECT_URL
            return settings.ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL
        else:
            return settings.ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL

    def after_confirmation(self, confirmation):
        user = confirmation.email_address.user
        user.is_active = True
        user.save()


class ChangePasswordView(FormView):

    template_name = "account/password_change.html"
    form_class = ChangePasswordForm
    redirect_field_name = "next"
    messages = {
        "password_changed": {
            "level": messages.SUCCESS,
            "text": _("Password successfully changed.")
        }
    }

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect("account_password_reset")
        return super(ChangePasswordView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return HttpResponseForbidden()
        return super(ChangePasswordView, self).post(*args, **kwargs)

    def change_password(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data["password_new"])
        user.save()

    def after_change_password(self):
        user = self.request.user
        signals.password_changed.send(sender=ChangePasswordView, user=user)
        if settings.ACCOUNT_NOTIFY_ON_PASSWORD_CHANGE:
            self.send_email(user)
        if self.messages.get("password_changed"):
            messages.add_message(
                self.request,
                self.messages["password_changed"]["level"],
                self.messages["password_changed"]["text"]
            )

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = {"user": self.request.user, "initial": self.get_initial()}
        if self.request.method in ["POST", "PUT"]:
            kwargs.update({
                "data": self.request.POST,
                "files": self.request.FILES,
            })
        return kwargs

    def form_valid(self, form):
        self.change_password(form)
        self.after_change_password()
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)

    def send_email(self, user):

        protocol = getattr(settings, "DEFAULT_HTPROTOCOL", "http")
        current_site = get_current_site(self.request)
        ctx = {
            "user": user,
            "protocol": protocol,
            "current_site": current_site,
        }
        hookset.send_password_change_email([user.email], ctx)


class PasswordResetView(FormView):

    template_name = "account/password_reset.html"
    template_name_sent = "account/password_reset_sent.html"
    form_class = PasswordResetForm
    token_generator = default_token_generator

    def get_context_data(self, **kwargs):
        context = kwargs
        if self.request.method == "POST" and "resend" in self.request.POST:
            context["resend"] = True
        return context

    def form_valid(self, form):
        self.send_email(form.cleaned_data["email"])
        response_kwargs = {
            "request": self.request,
            "template": self.template_name_sent,
            "context": self.get_context_data(form=form)
        }
        return self.response_class(**response_kwargs)

    def send_email(self, email):
        
        User = get_user_model()
        protocol = getattr(settings, "DEFAULT_HTPROTOCOL", "http")
        current_site = get_current_site(self.request)
        email_qs = EmailAddress.objects.filter(email__iexact=email)
        for user in User.objects.filter(pk__in=email_qs.values("user")):
            uid = int_to_base36(user.id)
            token = self.make_token(user)
            password_reset_url = "{0}://{1}{2}".format(
                protocol,
                current_site.domain,
                reverse("account_password_reset_token", kwargs=dict(uidb36=uid, token=token))
            )
            ctx = {
                "user": user,
                "current_site": current_site,
                "password_reset_url": password_reset_url,
            }
            hookset.send_password_reset_email([email], ctx)

    def make_token(self, user):
        return self.token_generator.make_token(user)


class PasswordResetTokenView(FormView):

    template_name = "account/password_reset_token.html"
    template_name_fail = "account/password_reset_token_fail.html"
    form_class = PasswordResetTokenForm
    token_generator = default_token_generator
    redirect_field_name = "next"
    messages = {
        "password_changed": {
            "level": messages.SUCCESS,
            "text": _("Password successfully changed.")
        },
    }

    def get(self, request, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ctx = self.get_context_data(form=form)
        if not self.check_token(self.get_user(), self.kwargs["token"]):
            return self.token_fail()
        return self.render_to_response(ctx)

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "uidb36": self.kwargs["uidb36"],
            "token": self.kwargs["token"],
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def change_password(self, form):
        user = self.get_user()
        user.set_password(form.cleaned_data["password"])
        user.save()

    def after_change_password(self):
        user = self.get_user()
        signals.password_changed.send(sender=PasswordResetTokenView, user=user)
        if self.messages.get("password_changed"):
            messages.add_message(
                self.request,
                self.messages["password_changed"]["level"],
                self.messages["password_changed"]["text"]
            )

    def form_valid(self, form):
        self.change_password(form)
        self.after_change_password()
        return redirect(self.get_success_url())

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_PASSWORD_RESET_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)

    def get_user(self):
        try:
            uid_int = base36_to_int(self.kwargs["uidb36"])
        except ValueError:
            raise Http404()
        return get_object_or_404(get_user_model(), id=uid_int)

    def check_token(self, user, token):
        return self.token_generator.check_token(user, token)

    def token_fail(self):
        response_kwargs = {
            "request": self.request,
            "template": self.template_name_fail,
            "context": self.get_context_data()
        }
        return self.response_class(**response_kwargs)


class SettingsView(LoginRequiredMixin, FormView):

    template_name = "account/settings.html"
    form_class = SettingsForm
    redirect_field_name = "next"
    messages = {
        "settings_updated": {
            "level": messages.SUCCESS,
            "text": _("Account settings updated.")
        },
    }

    def get_form_class(self):
        # @@@ django: this is a workaround to not having a dedicated method
        # to initialize self with a request in a known good state (of course
        # this only works with a FormView)
        self.primary_email_address = EmailAddress.objects.get_primary(self.request.user)
        return super(SettingsView, self).get_form_class()

    def get_initial(self):
        initial = super(SettingsView, self).get_initial()
        if self.primary_email_address:
            initial["email"] = self.primary_email_address.email
        return initial

    def form_valid(self, form):
        self.update_settings(form)
        if self.messages.get("settings_updated"):
            messages.add_message(
                self.request,
                self.messages["settings_updated"]["level"],
                self.messages["settings_updated"]["text"]
            )
        return redirect(self.get_success_url())

    def update_settings(self, form):
        self.update_email(form)
        self.update_account(form)

    def update_email(self, form, confirm=None):
        user = self.request.user
        if confirm is None:
            confirm = settings.ACCOUNT_EMAIL_CONFIRMATION_EMAIL
        # @@@ handle multiple emails per user
        email = form.cleaned_data["email"].strip()
        if not self.primary_email_address:
            user.email = email
            EmailAddress.objects.add_email(self.request.user, email, primary=True, confirm=confirm)
            user.save()
        else:
            if email != self.primary_email_address.email:
                self.primary_email_address.change(email, confirm=confirm)

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value": self.request.REQUEST.get(redirect_field_name, ""),
        })
        return ctx

    def update_account(self, form):
        account = self.request.user.account
        user = self.request.user
        mobile_number = form.cleaned_data["mobile_number"]
        if account:
            self.request.user.account.mobile_number = mobile_number
            # for k, v in fields.items():
                # setattr(account, k, v)
        account.save()

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def get_success_url(self, fallback_url=None, **kwargs):
        if fallback_url is None:
            fallback_url = settings.ACCOUNT_SETTINGS_REDIRECT_URL
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)


class DeleteView(LogoutView):

    template_name = "account/delete.html"
    messages = {
        "account_deleted": {
            "level": messages.WARNING,
            "text": _("Your account is now inactive and your data will be expunged in the next {expunge_hours} hours.")
        },
    }

    def post(self, *args, **kwargs):
        AccountDeletion.mark(self.request.user)
        auth.logout(self.request)
        messages.add_message(
            self.request,
            self.messages["account_deleted"]["level"],
            self.messages["account_deleted"]["text"].format(**{
                "expunge_hours": settings.ACCOUNT_DELETION_EXPUNGE_HOURS,
            })
        )
        return redirect(self.get_redirect_url())

    def get_context_data(self, **kwargs):
        ctx = super(DeleteView, self).get_context_data()
        ctx.update(kwargs)
        ctx["ACCOUNT_DELETION_EXPUNGE_HOURS"] = settings.ACCOUNT_DELETION_EXPUNGE_HOURS
        return ctx


def register_import(request):
    # import ipdb
    # ipdb.set_trace()
    reader = csv.reader(open("/home/suji/register_final.csv", "rb"))
    for row in reader:
        a = User.objects.create()
        a.username = row[0]
        a.set_password(row[1])
        a.save()
        if int(row[8]) == 1:
            b = Account.objects.create(user_id = a.id, mobile_number = 0, associated_with = row[7], user_category_id = 1)
            b.save()
        if int(row[8]) == 2:
            b = Account.objects.create(user_id = a.id, mobile_number = 0, associated_with = row[6], user_category_id = 2)
            b.save()
        if int(row[8]) == 3:
            b = Account.objects.create(user_id = a.id, mobile_number = 0, associated_with = row[5], user_category_id = 3)
            b.save()
   

    return render(request,"homepage.html")

def student_count_update(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()            
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()           
    school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
    for schl in school_list:
        cursor2.execute("INSERT INTO students_school_child_count (school_id,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,total_count) values (%s,0,0,0,0,0,0,0,0,0,0,0,0,0)",[schl.id])
        transaction.commit_unless_managed()

    return render(request,"homepage.html")


def photo_update(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()            
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()           
    school_list = School.objects.filter(block_id=request.user.account.associated_with).order_by('school_name')
    for schl in school_list:
        # cursor2.execute("INSERT INTO students_school_child_count (school_id,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,total_count) values (%s,0,0,0,0,0,0,0,0,0,0,0,0,0)",[schl.id])
        # transaction.commit_unless_managed()

        child = Child_detail.objects.filter(school=schl.id)

        for chld in child:
            cursor1.execute("update students_child_detail set photograph='images/child_pics/Kuruvikulam/%s/%s.jpg' where unique_id_no=%s", [chld.school.school_code,chld.unique_id_no,chld.unique_id_no])
            transaction.commit_unless_managed()

    return render(request,"homepage.html")

def generate_unique_id(request):
    #import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        from django.db import connection, transaction
        cursor = connection.cursor()
        school_id= School.objects.get(school_code=request.GET["school_code"])
        students = Child_detail.objects.filter(school=school_id.id).order_by('id')
        try:
            # cursor.execute("update webapp_school set student_id_count=0 where school_code=%s", [request.GET["school_code"]])
            # transaction.commit_unless_managed()
            recent_id=School.objects.get(school_code__exact=request.GET["school_code"])
        except Exception: 
            recent_id='00000'
        for entry in range(len(students)):

            current_id = str(int(recent_id.student_id_count)+1)
            unique_id=recent_id.school_code

            if len(current_id) < 5:
                if len(current_id) == 4:
                    current_id = '0'+current_id
                elif len(current_id) == 3:
                    current_id = '00'+current_id
                elif len(current_id) == 2:
                    current_id = '000'+current_id
                elif len(current_id) == 1:
                    current_id = '0000'+current_id

            uniqueid = str(unique_id)+current_id
            cursor.execute("update students_child_detail set unique_id_no=%s where school_id=%s and id=%s", [uniqueid,school_id.id,students[entry].id])
            transaction.commit_unless_managed()
            recent_id.student_id_count = current_id
            recent_id.save()
        # school_name=Register.objects.get(username__exact=request.GET["school_code2"])
        # block_name= School.objects.get(school_code__exact=request.GET["school_code2"])
        # block=block_name.habitation.block.block_name
        # students = Child_detail.objects.filter(block=block,location_code__exact=request.GET["school_code2"]).order_by('id')
        # try:
        #   cursor.execute("update webapp_school set student_id_count=0 where school_code=%s", [request.GET["school_code2"]])
        #   transaction.commit_unless_managed()
        #   recent_id=School.objects.get(school_code__exact=request.GET["school_code2"])
        # except Exception:
        #   recent_id='00000'
        # for entry in range(len(students)):

        #   current_id = str(int(recent_id.student_id_count)+1)
        #   unique_id=recent_id.school_code

        #   if len(current_id) < 5:
        #       if len(current_id) == 4:
        #           current_id = '0'+current_id
        #       elif len(current_id) == 3:
        #           current_id = '00'+current_id
        #       elif len(current_id) == 2:
        #           current_id = '000'+current_id
        #       elif len(current_id) == 1:
        #           current_id = '0000'+current_id

        #   uniqueid = unique_id+current_id
        #   cursor.execute("update webapp_child_detail set unique_id_no=%s where block=%s and id=%s", [uniqueid,block,students[entry].id])
        #   transaction.commit_unless_managed()
        #   recent_id.student_id_count = current_id
        #   recent_id.save()
        return HttpResponse(len(students))



# def tnschools_mail(request) :
#     # username = "praba"
#     # password = "rainbow"
#     username = str(33010500702)
#     password = str(1)
#     user = authenticate(username=username, password=password)
#     login('http://mail.tnschools.gov.in/mail/', user)
    
#     return HttpResponseRedirect('http://mail.tnschools.gov.in/mail/')


# import urllib
# import urllib2
# import ClientCookie
 
# def tnschools_mail(request):
#     url = "http://mail.tnschools.gov.in/mail/"  # example url
 
#     opts = {
#     'user': 'praba',
#     'password': 'rainbow'
#     # 'server': 'serverName'
#     }
 
#     data = urllib.urlencode(opts)
 
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12',
#     'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
#     'Accept-Language': 'en-gb,en;q=0.5',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
#     'Connection': 'keep-alive'
#     }
 
#     req = urllib2.Request(url, data)
 
#     response = urllib2.urlopen(req)
#     return response.read()