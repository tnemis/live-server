from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",
    #url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),

    url(r"^$", login_required(TemplateView.as_view(template_name="homepage.html")), name="home"),

    url(r"^admin/", include(admin.site.urls)),
    url(r"^accounts/", include("emis_account.urls")),
    url(r"^students/", include("students.urls")),
    url(r"^teachers/", include("teacher.urls")),
    url(r"^school/", include("school.urls")),
    url(r"^reports/", include("reports.urls")),
    url(r"^bus_pass/", include("bus_pass.urls")),
    url(r"^udise/", include("udise.urls")),
    url(r"^pool/", include("pool.urls")),
    url(r"^progress/", include("progress.urls")),
    url(r"^reports_basic/", include("reports_basic.urls")),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^messages/', include('postman.urls')),
    url(r"^access_denied/$", login_required(TemplateView.as_view(template_name="access_denied.html")), name="home"),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r"^helpdesk/", include("helpdesk.urls")),
    url(r'session_security/', include('session_security.urls')),
    url(r'^sessions/', include('session_activity.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
