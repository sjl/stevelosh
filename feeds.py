from django.contrib.syndication.feeds import Feed
from stevelosh.blog.models import Entry, Comment as BlogComment

class LatestEntries(Feed):
    title = "stevelosh.com blog entries"
    link = "http://stevelosh.com/blog/"
    description = "Latest blog entries on stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com/'
    
    def items(self):
        return Entry.objects.filter(published=True).order_by('-pub_date')[:15]
    
    def item_pubdate(self, item):
        return item.pub_date
