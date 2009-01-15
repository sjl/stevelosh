from django.db import models
import datetime

class TextThought(models.Model):
    title = models.CharField(blank=True, null=True, max_length=1000)
    posted = models.DateTimeField()
    body = models.TextField()
    tumblr_id = models.IntegerField(blank=False, null=False)
    type = models.CharField(default='text', max_length=100)
    
    def get_absolute_url(self):
        return u'/thoughts/#text-' + str(self.id)
    
    def __unicode__(self):
        return u'%s' % (self.body[:20],)

class LinkThought(models.Model):
    name = models.CharField(blank=True, null=True, max_length=1000)
    posted = models.DateTimeField()
    url = models.URLField(blank=False, verify_exists=False)
    description = models.TextField(blank=True, null=True)
    tumblr_id = models.IntegerField(blank=False, null=False)
    type = models.CharField(default='link', max_length=100)
    
    def get_absolute_url(self):
        return u'/thoughts/#text-' + str(self.id)
    
    def __unicode__(self):
        return u'%s' % (self.url,)

