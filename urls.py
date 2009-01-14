from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from stevelosh.feeds import LatestEntries


admin.autodiscover()
feeds = { 'blog': LatestEntries, }

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    url(r'^blog/$',                'stevelosh.blog.views.list',      name='blog-list-newest'),
    url(r'^blog/page/(\d+)/$',     'stevelosh.blog.views.list',      name='blog-list-page'),
    url(r'^blog/comment/$',        'stevelosh.blog.views.comment'),
    url(r'^blog/entry/(\d+)/(\d+)/(\d+)/(.*)/$',
                                   'stevelosh.blog.views.entry',     name='blog-entry'),
    url(r'^blog/(\d+)/(\d+)/(\d+)/(.*).html/$',
                                   'stevelosh.blog.views.old_entry', name='blog-old-entry'),
    url(r'^projects/$',            'stevelosh.projects.views.list',  name='project-list'),
    url(r'^projects/comment/$',    'stevelosh.projects.views.comment'),
    url(r'^projects/(.*)/$',       'stevelosh.projects.views.project'),
    url(r'^thoughts/$',            'stevelosh.thoughts.views.list',  name='thoughts-list-newest'),
    url(r'^thoughts/page/(\d+)/$', 'stevelosh.thoughts.views.list',  name='thoughts-list-page'),
    url(r'^rss/(?P<url>.*)/$',     'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )