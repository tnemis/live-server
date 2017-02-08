import os
from django.forms import Field
from django.utils.translation import ugettext_lazy
#Form Error message override
Field.default_error_messages = {
    'required': ugettext_lazy("This field is mandatory."),
    'caps': 'This field if case sensitive'
}

import os
os.environ['http_proxy']='http://10.236.245.251:9191'
os.environ['https_proxy']='https://10.236.245.251:9191'

DIRNAME = os.path.dirname(__file__)

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'ta'
ugettext = lambda s: s
LANGUAGES = (
    ('ta', ugettext("Tamil")),
    ('en', ugettext("English")),

)

LOCALE_PATHS = [
    DIRNAME + '/locale',
]

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [
    # ("Your Name", "your_email@example.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {

        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "semis_db",
        "USER": "emisnew_user",
        "PASSWORD": "emisnew_user",
        "HOST": "",
        "PORT": "",


#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "emis_working",
#         "USER": "postgres",
# #	"PASSWORD": "password123",
#         "HOST": "10.236.247.134",
#         'CONN_MAX_AGE': 60,
#         "PORT": "5433",
    }
}


ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Asia/Calcutta"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html


SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

DATE_INPUT_FORMATS = ('%d/%m/%Y',)
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "(-!jg)aqm5yys)m6h9vqg65t6wnvmnd@aywrfg#&i^269vtr5-"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "emis_account.context_processors.account",
    'django.core.context_processors.request',
    'postman.context_processors.inbox',

]


MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    'axes.middleware.FailedLoginMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'session_activity.middleware.SessionActivityMiddleware',
]


ROOT_URLCONF = "emis.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "emis.wsgi.application"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

INSTALLED_APPS = [
    "django_admin_bootstrapped",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "widget_tweaks",
    'report_builder',
    'easy_pjax',
    'smart_selects',
    'csvimport',
    #"sslserver",
    # theme


    # external
    "emis_account",
    "eventlog",
    "metron",
    'postman',
    'notification',
    'mailer',
    'braces',
    'django_extensions',

    'helpdesk',
    'django_markup',
    'markup_deprecated',
    'django_markdown',
    'axes',
    'session_security',
    'session_activity',
    # 'cerberos',

    # project
    "emis",
    "students",
    "baseapp",
    "imagekit",
    "teacher",
    "school",
    "reports",
    "reports_basic",
    "bus_pass",
    'udise',
    'pool',
    'progress',

    ]

REPORT_BUILDER_GLOBAL_EXPORT=True

CACHEOPS_DEGRADE_ON_FAILURE=True
CACHEOPS_REDIS = {
    'host': '10.236.247.239', # redis-server is on same machine
    'port': 6379,        # default redis port
    'db': 1,             # SELECT non-default redis database
                         # using separate redis db or redis instance
                         # is highly recommended
    'socket_timeout': 60,
}

CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 5 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User
    'auth.user': ('get', 60*5),

    # Automatically cache all gets, queryset fetches and counts
    # to other django.contrib.auth models for 10 mins
    'auth.*': ('all', 60*10),

    # Enable manual caching on all news models with default timeout of an hour
    # Use News.objects.cache().get(...)
    #  or Tags.objects.filter(...).order_by(...).cache()
    # to cache particular ORM request.
    # Invalidation is still automatic


    # Automatically cache count requests for all other models for 5 min
    '*.*': ('all', 60*5),
}
SMS_GATEWAY_USERNAME = '2000075773'
SMS_GATEWAY_PASSWORD = 'MLuiuYleB'
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
SESSION_ENGINE = 'redis_sessions.session'
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}


# django helpdesk

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = (
            global_settings.TEMPLATE_CONTEXT_PROCESSORS +
            ('django.core.context_processors.request',)
     )
HELPDESK_DEFAULT_SETTINGS = {
        'use_email_as_submitter': True,
        'email_on_ticket_assign': True,
        'email_on_ticket_change': True,
        'login_view_ticketlist': True,
        'email_on_ticket_apichange': True,
        'tickets_per_page': 25
        }

HELPDESK_SUBMIT_A_TICKET_PUBLIC = True

# django helpdesk ends here

SESSION_COOKIE_PATH = '/;HttpOnly'
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]
EMAIL_BACKEND = "mailer.backend.DbBackend"
DEFAULT_FROM_EMAIL = 'Tnschools.gov.in<no-reply@tnschools.gov.in>'
#EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
#smtp is the default email backend.But,here I am setting this explicitly.
EMAIL_HOST = 'mail.tnschools.gov.in'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'no-reply@tnschools.gov.in'
EMAIL_HOST_PASSWORD = 'no-reply@2014'
EMAIL_USE_TLS = True
ACCOUNT_TIMEZONES = ["UTC","UTC",]
ACCOUNT_LANGUAGES = ["Tamil","ENGLISH",]
ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_CREATE_ON_SAVE= True
ACCOUNT_EMAIL_CONFIRMATION_EMAIL=True
ACCOUNT_SIGNUP_REDIRECT_URL='/'
ACCOUNT_USER_DISPLAY = lambda user: user.username
ACCOUNT_PASSWORD_RESET_REDIRECT_URL='/'
ACCOUNT_NOTIFY_ON_PASSWORD_CHANGE = True
ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = '/'
ACCOUNT_LOGIN_URL = '/'
ACCOUNT_SETTINGS_REDIRECT_URL = '/'

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/accounts/login/'

AUTHENTICATION_BACKENDS = [
    "emis_account.auth_backends.UsernameAuthenticationBackend",
]

SESSION_SECURITY_WARN_AFTER = 800
SESSION_SECURITY_EXPIRE_AFTER = 900
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MAX_FAILED_LOGINS = 3
MEMORY_FOR_FAILED_LOGINS = 120

AXES_LOGIN_FAILURE_LIMIT = 3
AXES_COOLOFF_TIME = 1



#POSTMAN configuration
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_DISALLOW_MULTIRECIPIENTS=False
POSTMAN_DISALLOW_COPIES_ON_REPLY=False
POSTMAN_DISABLE_USER_EMAILING = False
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_SHOW_USER_AS = None
POSTMAN_QUICKREPLY_QUOTE_BODY = False
POSTMAN_NOTIFIER_APP='notification'
POSTMAN_MAILER_APP = 'mailer'
#POSTMAN_AUTOCOMPLETER_APP=


#CRON
#* * * * * (cd /home/praba/web/app/emis/;/home/praba/.virtualenv/emis/bin/python manage.py send_mail >> ~/cron_mail.log 2>&1)
#0,20,40 * * * * (cd /home/praba/web/app/emis/;/home/praba/.virtualenv/emis/bin/python manage.py retry_deferred >> ~/cron_mail_deferred.log 2>&1)
# Edit this file to introduce tasks to be run by cron.
