from django.contrib.syndication.feeds import Feed
from stevelosh.blog.models import Entry, Comment as BlogComment
from stevelosh.projects.models import Project, Comment as ProjectComment
from stevelosh.thoughts.models import TextThought, LinkThought
import operator

class LatestEntries(Feed):
    title = "stevelosh.com blog entries"
    link = "http://stevelosh.com/blog/"
    description = "Latest blog entries on stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com/'
    
    def items(self):
        return Entry.objects.filter(published=True).order_by('-pub_date')[:10]
    
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
        comments  = list(BlogComment.objects.order_by('-submitted')[:50])
        comments += list(ProjectComment.objects.order_by('-submitted')[:50])
        comments.sort(key=operator.attrgetter('submitted'))
        comments.reverse()
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
        return Project.objects.order_by('-posted')[:10]
    
    def item_pubdate(self, item):
        return item.posted
    

class LatestThoughts(Feed):
    title = "stevelosh.com thoughts"
    link = "http://stevelosh.com/thoughts/"
    description = "Latest thoughts from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com/'
    
    def items(self):
        thoughts = []
        thoughts += [{'type': 'thought-text', 'item': thought, 'date': thought.posted}
                     for thought in 
                     TextThought.objects.order_by('-posted')[:10]]
        thoughts += [{'type': 'thought-link', 'item': thought, 'date': thought.posted}
                     for thought in 
                     LinkThought.objects.order_by('-posted')[:10]]
        thoughts.sort(key=operator.itemgetter('date'))
        thoughts.reverse()
        return thoughts[:10]
    
    def item_pubdate(self, item):
        return item['date']
    
    def item_link(self, item):
        return item['item'].get_absolute_url()
    

class LatestEverything(Feed):
    title = "stevelosh.com"
    link = "http://stevelosh.com/"
    description = "Latest updates from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com/'
    
    def items(self):
        items = []
        items += [{'type': 'blog', 'item': entry, 'date': entry.pub_date} 
                  for entry in 
                  Entry.objects.filter(published=True).order_by('-pub_date')[:15]]
        items += [{'type': 'thought-text', 'item': thought, 'date': thought.posted}
                  for thought in 
                  TextThought.objects.order_by('-posted')[:10]]
        items += [{'type': 'thought-link', 'item': thought, 'date': thought.posted}
                  for thought in 
                  LinkThought.objects.order_by('-posted')[:10]]
        items += [{'type': 'project', 'item': project, 'date': project.posted}
                  for project in 
                  Project.objects.order_by('-posted')[:10]]
        items.sort(key=operator.itemgetter('date'))
        items.reverse()
        return items[:10]
    
    def item_pubdate(self, item):
        return item['date']
    
    def item_link(self, item):
        return item['item'].get_absolute_url()
