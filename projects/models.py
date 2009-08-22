from django.db import models
import datetime


class Project(models.Model):
    """A model of a project."""
    
    name = models.CharField(blank=False, max_length=140)
    snip = models.CharField(blank=False, max_length=140)
    type = models.CharField(blank=True, max_length=15)
    body = models.TextField(blank=True)
    posted = models.DateTimeField(blank=False, default=datetime.datetime.now)
    slug = models.SlugField()
    
    @models.permalink
    def get_absolute_url(self):
        return ('project-view', (self.slug,),)
    
    def __unicode__(self):
        return u"%s" % (self.name,)


class Comment(models.Model):
    name = models.CharField(blank=False, null=False, max_length=40)
    body = models.TextField(blank=False, null=False)
    submitted = models.DateTimeField(default=datetime.datetime.now)
    project = models.ForeignKey(Project)
    spam = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return self.project.get_absolute_url() + "#comment-" + str(self.id)
    
    def __unicode__(self):
        return u'%s on %s' % (self.name, self.project.name)
    
    def snip(self):
        return self.body[:40] + '...' if len(self.body) > 40 else ''
    

