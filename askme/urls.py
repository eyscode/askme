from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()
from web.views import CreateQuestionView, ListQuestionView, DetailQuestionView

urlpatterns = patterns(
    '',
    url(r'^$', ListQuestionView.as_view(), name='index'),
    url(r'^preguntas/(?P<pk>\d+)/$', DetailQuestionView.as_view(), name='detail-ask'),
    url(r'^crear/$', CreateQuestionView.as_view(), name='ask'),
    # url(r'^admin/', include(admin.site.urls)),
)
