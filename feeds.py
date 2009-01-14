from django.contrib.syndication.feeds import Feed
from stevelosh.blog.models import Entry, Comment as BlogComment
from stevelosh.projects.models import Project, Comment as ProjectComment
import operator

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

class LatestComments(Feed):
    title = "stevelosh.com blog comments"
    link = "http://stevelosh.com/blog/"
    description = "Latest comments on blog entries from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com/'
    
    def items(self):
        comments = list(BlogComment.objects.order_by('-submitted')[:50])
        comments += list(ProjectComment.objects.order_by('-submitted')[:50])
        comments.sort(key=operator.attrgetter('submitted'))
        return comments[:50]
    
    def item_pubdate(self, item):
        return item.submitted

class LatestProjects(Feed):
    title = "stevelosh.com projects"
    link = "http://stevelosh.com/projects/"
    description = "Latest projects on stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com/'
    
    def items(self):
        return Project.objects.order_by('-posted')[:15]
    
    def item_pubdate(self, item):
        return item.posted
    
