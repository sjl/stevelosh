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


class ProjectFile(models.Model):
    """A single file for a project."""
    
    title = models.CharField(blank=False, max_length=140)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='storage/projects/files')
    project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return u"%s - %s" % (self.project.name, self.title)


class ProjectPhoto(models.Model):
    """A single photograph for a project."""
    
    title = models.CharField(blank=False, max_length=140)
    description = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='storage/projects/images',
                              height_field='height', width_field='width')
    project = models.ForeignKey(Project)
    position = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s - %s" % (self.project.name, self.title)


class Comment(models.Model):
    name = models.CharField(blank=False, null=False, max_length=40)
    body = models.TextField(blank=False, null=False)
    submitted = models.DateTimeField(default=datetime.datetime.now)
    project = models.ForeignKey(Project)
    
    def get_absolute_url(self):
        return self.project.get_absolute_url() + "#comment-" + str(self.id)
    
    def __unicode__(self):
        return u'%s on %s' % (self.name, self.entry.title)
    
