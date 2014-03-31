from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()
from web.views import FormAsk, ListAsk

urlpatterns = patterns(
    '',
    url(r'^$', ListAsk.as_view(), name='index'),
    url(r'^crear/$', FormAsk.as_view(), name='ask'),
    # url(r'^admin/', include(admin.site.urls)),
)
