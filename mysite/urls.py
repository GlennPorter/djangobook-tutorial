from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead
from books import views as books_views
from contact import views as contact_views

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^search/$', books_views.search),
    (r'^contact/$', contact_views.contact),
    (r'^contact/thanks/$', contact_views.contact_thanks),
)
