from django.contrib.syndication.feeds import Feed
from stevelosh.blog.models import Entry, Comment as BlogComment
from stevelosh.projects.models import Project, Comment as ProjectComment
import operator


class LatestComments(Feed):
    title = "Steve Losh / RSS / Comments"
    link = "http://stevelosh.com/blog"
    description = "Latest comments on blog entries from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
    def items(self):
        comments  = list(BlogComment.objects.filter(spam=False)
                                            .order_by('-submitted')[:10])
        comments += list(ProjectComment.objects.filter(spam=False)
                                               .order_by('-submitted')[:10])
        comments.sort(key=operator.attrgetter('submitted'))
        comments.reverse()
        return comments[:20]
    
    def item_pubdate(self, item):
        return item.submitted
    
    def item_link(self, item):
        return item.get_absolute_url()
    

class LatestEverything(Feed):
    title = "Steve Losh"
    link = "http://stevelosh.com"
    description = "Latest updates from stevelosh.com"
    
    item_author_name = 'Steve Losh'
    item_author_email = 'steve@stevelosh.com'
    item_author_link = 'http://stevelosh.com'
    
    def items(self):
        items = []
        
        items += [{'type': 'blog', 'item': entry, 'date': entry.pub_date, 'title': entry.title} 
            for entry in Entry.objects.filter(published=True).order_by('-pub_date')[:10]]
        
        items += [{'type': 'project', 'item': project, 'date': project.posted, 'title': project.name}
            for project in Project.objects.order_by('-posted')[:10]]
        
        items.sort(key=operator.itemgetter('date'))
        items.reverse()
        return items[:5]
    
    def item_pubdate(self, item):
        return item['date']
    
    def item_link(self, item):
        title = 'Steve Losh / ' + item['title']
        new_link = item['item'].get_absolute_url()
        
        return new_link
    
