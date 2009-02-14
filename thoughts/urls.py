from django.conf.urls.defaults import *

urlpatterns = patterns('stevelosh.thoughts.views',
    url(r'^$',            'list', name='thoughts-list-newest'),
    url(r'^page/(\d+)/$', 'list', name='thoughts-list-page'),
)