from django.conf.urls.defaults import *

urlpatterns = patterns('projects.views',
    url(r'^$',         'list',    name='project-list'),
    url(r'^comment/$', 'comment', name='project-post-comment'),
    url(r'^(.*)/$',    'project', name='project-view'),
)