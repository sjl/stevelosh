from django.conf.urls.defaults import *
from stevelosh.rss.feeds import *

feeds = { 'comments': LatestComments,
          'all': LatestEverything, }

urlpatterns = patterns('',
    url(r'^(?P<url>.+)/$', 'django.contrib.syndication.views.feed', 
        {'feed_dict': feeds}),
)