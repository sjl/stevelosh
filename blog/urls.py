from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$',                              'list',      name='blog-list-newest'),
    url(r'^page/(\d+)/$',                   'list',      name='blog-list-page'),
    url(r'^comment/$',                      'comment',   name='blog-post-comment'),
    url(r'^entry/(\d+)/(\d+)/(\d+)/(.*)/$', 'entry',     name='blog-entry'),
    url(r'^(\d+)/(\d+)/(\d+)/(.*).html/$',  'old_entry', name='blog-old-entry'),
)