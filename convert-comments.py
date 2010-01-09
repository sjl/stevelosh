#!/usr/bin/env python

from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site
from stevelosh.blog.models import Comment as BlogComment
from stevelosh.projects.models import Comment as ProjectComment


site = Site.objects.all()[0]
blog_comments = BlogComment.objects.filter(spam=False)
project_comments = ProjectComment.objects.filter(spam=False)

for bc in blog_comments:
    c = Comment()
    c.content_object = bc.entry
    c.user_name = bc.name
    c.comment = bc.body
    c.submit_date = bc.submitted
    c.site = site
    c.is_public = True
    c.is_removed = False
    c.save()
    print 'http://%s%s' % (site.domain, c.content_object.get_absolute_url())

for pc in project_comments:
    c = Comment()
    c.content_object = pc.project
    c.user_name = pc.name
    c.comment = pc.body
    c.submit_date = pc.submitted
    c.site = site
    c.is_public = True
    c.is_removed = False
    c.save()
    print 'http://%s%s' % (site.domain, c.content_object.get_absolute_url())
