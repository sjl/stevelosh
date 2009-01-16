from django.contrib.syndication.feeds import Feed
from stevelosh.blog.models import Entry, Comment as BlogComment
from stevelosh.projects.models import Project, Comment as ProjectComment
from stevelosh.thoughts.models import TextThought, LinkThought
import operator


feeder = "http://stevelosh.com/feeder"

class LatestEntries(Feed):
    title = "Steve Losh / RSS / Blog"
    link = "http://stevelosh.com/blog"
    description = "Latest blog entries on stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
    def items(self):
        return Entry.objects.filter(published=True).order_by('-pub_date')[:10]
    
    def item_pubdate(self, item):
        return item.pub_date
    
    def item_link(self, item):
        return '%s/?FeederAction=clicked&feed=%s&seed=%s&seed_title=%s' % \
               (feeder,
                'Blog', 
                self.item_author_link + item.get_absolute_url(), 
                'Steve Losh / ' + item.title)

class LatestComments(Feed):
    title = "Steve Losh / RSS / Comments"
    link = "http://stevelosh.com/blog"
    description = "Latest comments on blog entries from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
    def items(self):
        comments  = list(BlogComment.objects.order_by('-submitted')[:50])
        comments += list(ProjectComment.objects.order_by('-submitted')[:50])
        comments.sort(key=operator.attrgetter('submitted'))
        comments.reverse()
        return comments[:50]
    
    def item_pubdate(self, item):
        return item.submitted
    
    def item_link(self, item):
        return '%s/?FeederAction=clicked&feed=%s&seed=%s&seed_title=%s' % \
               (feeder,
                'Comments', 
                self.item_author_link + item.get_absolute_url(), 
                'Comment %d' % item.id)

class LatestProjects(Feed):
    title = "Steve Losh / RSS / Projects"
    link = "http://stevelosh.com/projects"
    description = "Latest projects on stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
    def items(self):
        return Project.objects.order_by('-posted')[:10]
    
    def item_pubdate(self, item):
        return item.posted
    
    def item_link(self, item):
        return '%s/?FeederAction=clicked&feed=%s&seed=%s&seed_title=%s' % \
               (feeder,
                'Projects', 
                self.item_author_link + item.get_absolute_url(), 
                'Steve Losh / ' + item.name)
    

class LatestThoughts(Feed):
    title = "Steve Losh / RSS / Thoughts"
    link = "http://stevelosh.com/thoughts"
    description = "Latest thoughts from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
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
        title = 'Steve Losh / '
        if item['type'] == 'thought-text':
            title += 'Thoughts / ' + item['item'].id
        elif item['type'] == 'thought-link':
            title += 'Thoughts / ' + item['item'].url
        
        return '%s/?FeederAction=clicked&feed=%s&seed=%s&seed_title=%s' % \
               (feeder,
                'Thoughts', 
                self.item_author_link + item['item'].get_absolute_url(), 
                title)
    

class LatestEverything(Feed):
    title = "Steve Losh / RSS / All"
    link = "http://stevelosh.com"
    description = "Latest updates from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
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
        title = 'Steve Losh / '
        if item['type'] == 'blog':
            title += item['item'].title
        elif item['type'] == 'project':
            title += item['item'].name
        elif item['type'] == 'thought-text':
            title += 'Thoughts / ' + item['item'].id
        elif item['type'] == 'thought-link':
            title += 'Thoughts / ' + item['item'].url
        
        return '%s/?FeederAction=clicked&feed=%s&seed=%s&seed_title=%s' % \
               (feeder,
                'All', 
                self.item_author_link + item['item'].get_absolute_url(), 
                title)
    
