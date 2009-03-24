from django.conf.urls.defaults import *
from stevelosh.rss.feeds import *

feeds = { 'blog': LatestEntries, 
          'comments': LatestComments,
          'projects': LatestProjects, 
          'all': LatestEverything, }

urlpatterns = patterns('stevelosh.rss.views',
    url(r'^(?P<url>.+)/$', 'feeds', {'feed_dict': feeds}),
)