from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()
from web.views import FormAsk, ListAsk

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'web.views.home', name='index'),
    url(r'^crear/$', 'web.views.form_ask', name='ask'),

    #CBVs
    url(r'^alternative/$', ListAsk.as_view(), name='index2'),
    url(r'^crear2/$', FormAsk.as_view(), name='ask2'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
