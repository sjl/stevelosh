from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import mobileadmin

admin.autodiscover()
mobileadmin.autoregister()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^m/(.*)', mobileadmin.sites.site.root),
    url(r'^blog/', include('stevelosh.blog.urls')),
    url(r'^projects/', include('stevelosh.projects.urls')),
    url(r'^thoughts/', include('stevelosh.thoughts.urls')),
    url(r'^rss/', include('stevelosh.rss.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

handler404 = 'mobileadmin.views.page_not_found'
handler500 = 'mobileadmin.views.server_error'
