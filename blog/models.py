from django.db import models
import datetime

class Entry(models.Model):
    title = models.CharField(max_length=140)
    snip = models.CharField(max_length=140)
    slug = models.SlugField()
    pub_date = models.DateTimeField('Date Published', 
                                    default=datetime.datetime.now)
    body = models.TextField()
    published = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return "/blog/entry/%i/%i/%i/%s/" % (self.pub_date.year, 
            self.pub_date.month, self.pub_date.day, self.slug)
    
    def __unicode__(self):
        return u'%s' % (self.title,)

class Comment(models.Model):
    name = models.CharField('Commenter', blank=False, null=False, 
                            max_length=40)
    body = models.TextField('Comment', blank=False, null=False)
    submitted = models.DateTimeField(default=datetime.datetime.now)
    entry = models.ForeignKey(Entry)
    
    def get_absolute_url(self):
        return self.entry.get_absolute_url() + "#comment-" + str(self.id)
    
    def __unicode__(self):
        return u'%s on %s' % (self.name, self.entry.title)

