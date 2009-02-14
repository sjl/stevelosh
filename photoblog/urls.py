from django.conf.urls.defaults import *

urlpatterns = patterns('stevelosh.photoblog.views',
    url(r'^$',                              'entry', name='photoblog-newest'),
    url(r'^entry/(\d+)/(\d+)/(\d+)/(.*)/$', 'entry', name='photoblog-entry'),
)
