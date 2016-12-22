from __future__ import unicode_literals
from django.core.exceptions import ValidationError
import datetime
import operator
import urllib

from django.core.urlresolvers import reverse
from django.db import models, transaction
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone, translation, six
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AnonymousUser
from django.contrib.sites.models import Site
from baseapp.models import School,Block,District
import pytz
from django.core import serializers
from emis_account import signals
from emis_account.compat import AUTH_USER_MODEL, get_user_model
from emis_account.conf import settings
from emis_account.fields import TimeZoneField
from emis_account.hooks import hookset
from emis_account.managers import EmailAddressManager, EmailConfirmationManager
from emis_account.signals import signup_code_sent, signup_code_used
from django.core.validators import MaxValueValidator, MinValueValidator #to validate min and max value


class Account(models.Model):

    user = models.OneToOneField(AUTH_USER_MODEL, related_name="account", verbose_name=_("user"))
    mobile_number = models.BigIntegerField(validators=[MinValueValidator(6000000000),MaxValueValidator(9999999999)])
    user_category = models.ForeignKey('User_Category')
    associated_with = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    
   
    @classmethod
    def for_request(cls, request):
        if request.user.is_authenticated():
            try:
                account = Account._default_manager.get(user=request.user)
            except Account.DoesNotExist:
                account = AnonymousAccount(request)
        else:
            account = AnonymousAccount(request)
        return account

    @classmethod
    def create(cls, request=None, **kwargs):
        create_email = kwargs.pop("create_email", True)
        confirm_email = kwargs.pop("confirm_email", None)
        account = cls(**kwargs)
        if create_email and account.user.email:
            kwargs = {"primary": True}
            if confirm_email is not None:
                kwargs["confirm"] = confirm_email
            EmailAddress.objects.add_email(account.user, account.user.email, **kwargs)
        
        return account
    def get_user_info(self):
        if str(self.user_category) == str('school'):
            user_associated_with = School.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('block'):
             #user_associated_with = serializers.serialize( "python", Block.objects.get(block_code=self.associated_with))
             user_associated_with = Block.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('edu_district'):
             user_associated_with = Block.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('cbse'):
             user_associated_with = Block.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('icse'):
             user_associated_with = Block.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('othr'):
             user_associated_with = Block.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('dee_district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('dse_district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('dms_district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('cbse_district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('icse_district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('othr_district'):
             user_associated_with = District.objects.get(id=self.associated_with)
        elif str(self.user_category) == str('state'):
             user_associated_with = "State"
        elif str(self.user_category) == str('dee_state'):
             user_associated_with = "State"
        elif str(self.user_category) == str('dse_state'):
             user_associated_with = "State"
        elif str(self.user_category) == str('dms_state'):
             user_associated_with = "State"
        elif str(self.user_category) == str('cbse_state'):
             user_associated_with = "State"
        elif str(self.user_category) == str('icse_state'):
             user_associated_with = "State"
        elif str(self.user_category) == str('othr_state'):
             user_associated_with = "State"
             
        return  user_associated_with
    def __unicode__(self):
        try:
            if not self.get_user_info():
                raise ValidationError('Associated_with ID does not match with the user category')
        except Exception:
            raise ValidationError('Associated_with ID does not match with the user category')
            #user_associated_with = user_associated_with.school_name
        return u'%s' %(self.user)

    
#
# The call to get_user_model in global scope could lead to a circular import
# when the app cache is not fully initialized in some cases. It is rare, but
# it has happened. If you are debugging this problem and determine this line
# of code as being problematic, contact the developers right away.
#
@receiver(post_save, sender=get_user_model())
def user_post_save(sender, **kwargs):
    """
    After User.save is called we check to see if it was a created user. If so,
    we check if the User object wants account creation. If all passes we
    create an Account object.
    
    We only run on user creation to avoid having to check for existence on
    each call to User.save.
    """
    user, created = kwargs["instance"], kwargs["created"]
    disabled = getattr(user, "_disable_account_creation", not settings.ACCOUNT_CREATE_ON_SAVE)
    if created and not disabled:
        Account.create(user=user)


class AnonymousAccount(object):

    def __init__(self, request=None):
        self.user = AnonymousUser()
        self.timezone = settings.TIME_ZONE
        if request is None:
            self.language = settings.LANGUAGE_CODE
        else:
            self.language = translation.get_language_from_request(request, check_path=True)

    def __unicode__(self):
        return "AnonymousAccount"


class SignupCode(models.Model):

    class AlreadyExists(Exception):
        pass

    class InvalidCode(Exception):
        pass

    code = models.CharField(max_length=64, unique=True)
    max_uses = models.PositiveIntegerField(default=0)
    expiry = models.DateTimeField(null=True, blank=True)
    inviter = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    sent = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    use_count = models.PositiveIntegerField(editable=False, default=0)

    def __unicode__(self):
        if self.email:
            return "{0} [{1}]".format(self.email, self.code)
        else:
            return self.code

    @classmethod
    def exists(cls, code=None, email=None):
        checks = []
        if code:
            checks.append(Q(code=code))
        if email:
            checks.append(Q(email=code))
        return cls._default_manager.filter(six.moves.reduce(operator.or_, checks)).exists()

    @classmethod
    def create(cls, **kwargs):
        email, code = kwargs.get("email"), kwargs.get("code")
        if kwargs.get("check_exists", True) and cls.exists(code=code, email=email):
            raise cls.AlreadyExists()
        expiry = timezone.now() + datetime.timedelta(hours=kwargs.get("expiry", 24))
        if not code:
            code = hookset.generate_signup_code_token(email)
        params = {
            "code": code,
            "max_uses": kwargs.get("max_uses", 0),
            "expiry": expiry,
            "inviter": kwargs.get("inviter"),
            "notes": kwargs.get("notes", "")
        }
        if email:
            params["email"] = email
        return cls(**params)

    @classmethod
    def check(cls, code):
        try:
            signup_code = cls._default_manager.get(code=code)
        except cls.DoesNotExist:
            raise cls.InvalidCode()
        else:
            if signup_code.max_uses and signup_code.max_uses <= signup_code.use_count:
                raise cls.InvalidCode()
            else:
                if signup_code.expiry and timezone.now() > signup_code.expiry:
                    raise cls.InvalidCode()
                else:
                    return signup_code

    def calculate_use_count(self):
        self.use_count = self.signupcoderesult_set.count()
        self.save()

    def use(self, user):
        """
        Add a SignupCode result attached to the given user.
        """
        result = SignupCodeResult()
        result.signup_code = self
        result.user = user
        result.save()
        signup_code_used.send(sender=result.__class__, signup_code_result=result)

    def send(self, **kwargs):
        protocol = getattr(settings, "DEFAULT_HTPROTOCOL", "http")
        current_site = kwargs["site"] if "site" in kwargs else Site.objects.get_current()
        signup_url = "{0}://{1}{2}?{3}".format(
            protocol,
            current_site.domain,
            reverse("account_signup"),
            urllib.urlencode({"code": self.code})
        )
        ctx = {
            "signup_code": self,
            "current_site": current_site,
            "signup_url": signup_url,
        }
        hookset.send_invitation_email([self.email], ctx)
        self.sent = timezone.now()
        self.save()
        signup_code_sent.send(sender=SignupCode, signup_code=self)


class SignupCodeResult(models.Model):

    signup_code = models.ForeignKey(SignupCode)
    user = models.ForeignKey(AUTH_USER_MODEL)
    timestamp = models.DateTimeField(default=timezone.now)

    def save(self, **kwargs):
        super(SignupCodeResult, self).save(**kwargs)
        self.signup_code.calculate_use_count()


class EmailAddress(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL)
    email = models.EmailField(unique=settings.ACCOUNT_EMAIL_UNIQUE)
    verified = models.BooleanField(default=False)
    primary = models.BooleanField(default=False)

    objects = EmailAddressManager()

    class Meta:
        verbose_name = _("email address")
        verbose_name_plural = _("email addresses")
        if not settings.ACCOUNT_EMAIL_UNIQUE:
            unique_together = [("user", "email")]

    def __unicode__(self):
        return "{0} ({1})".format(self.email, self.user)

    def set_as_primary(self, conditional=False):
        old_primary = EmailAddress.objects.get_primary(self.user)
        if old_primary:
            if conditional:
                return False
            old_primary.primary = False
            old_primary.save()
        self.primary = True
        self.save()
        self.user.email = self.email
        self.user.save()
        return True

    def send_confirmation(self, **kwargs):
        confirmation = EmailConfirmation.create(self)
        confirmation.send(**kwargs)
        return confirmation

    def change(self, new_email, confirm=True):
        """
        Given a new email address, change self and re-confirm.
        """
        with transaction.commit_on_success():
            self.user.email = new_email
            self.user.save()
            self.email = new_email
            self.verified = False
            self.save()
            if confirm:
                self.send_confirmation()


class EmailConfirmation(models.Model):

    email_address = models.ForeignKey(EmailAddress)
    created = models.DateTimeField(default=timezone.now())
    sent = models.DateTimeField(null=True)
    key = models.CharField(max_length=64, unique=True)

    objects = EmailConfirmationManager()

    class Meta:
        verbose_name = _("email confirmation")
        verbose_name_plural = _("email confirmations")

    def __unicode__(self):
        return "confirmation for {0}".format(self.email_address)

    @classmethod
    def create(cls, email_address):
        key = hookset.generate_email_confirmation_token(email_address.email)
        return cls._default_manager.create(email_address=email_address, key=key)

    def key_expired(self):
        expiration_date = self.sent + datetime.timedelta(days=settings.ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS)
        return expiration_date <= timezone.now()
    key_expired.boolean = True

    def confirm(self):
        if not self.key_expired() and not self.email_address.verified:
            email_address = self.email_address
            email_address.verified = True
            email_address.set_as_primary(conditional=True)
            email_address.save()
            signals.email_confirmed.send(sender=self.__class__, email_address=email_address)
            return email_address

    def send(self, **kwargs):
        current_site = kwargs["site"] if "site" in kwargs else Site.objects.get_current()
        protocol = getattr(settings, "DEFAULT_HTPROTOCOL", "http")
        activate_url = "{0}://{1}{2}".format(
            protocol,
            current_site.domain,
            reverse("account_confirm_email", args=[self.key])
        )
        ctx = {
            "email_address": self.email_address,
            "user": self.email_address.user,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": self.key,
        }
        hookset.send_confirmation_email([self.email_address.email], ctx)
        self.sent = timezone.now()
        self.save()
        signals.email_confirmation_sent.send(sender=self.__class__, confirmation=self)


class AccountDeletion(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    date_requested = models.DateTimeField(default=timezone.now)
    date_expunged = models.DateTimeField(null=True, blank=True)

    @classmethod
    def expunge(cls, hours_ago=None):
        if hours_ago is None:
            hours_ago = settings.ACCOUNT_DELETION_EXPUNGE_HOURS
        before = timezone.now() - datetime.timedelta(hours=hours_ago)
        count = 0
        for account_deletion in cls.objects.filter(date_requested__lt=before, user__isnull=False):
            settings.ACCOUNT_DELETION_EXPUNGE_CALLBACK(account_deletion)
            account_deletion.date_expunged = timezone.now()
            account_deletion.save()
            count += 1
        return count

    @classmethod
    def mark(cls, user):
        account_deletion, created = cls.objects.get_or_create(user=user)
        account_deletion.email = user.email
        account_deletion.save()
        settings.ACCOUNT_DELETION_MARK_CALLBACK(account_deletion)
        return account_deletion

"""
Model for user category
"""
class User_Category(models.Model):
    user_category = models.CharField(max_length=15)
    def __unicode__(self):
        return u'%s' % (self.user_category)
