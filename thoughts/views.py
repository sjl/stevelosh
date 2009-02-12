from stevelosh.thoughts.models import TextThought, LinkThought
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
import operator

ENTRIES_PER_PAGE = 10

def list(request, page=1):
    page = int(page)
    
    thoughts = []
    thoughts += TextThought.objects.all().order_by('-posted')
    thoughts += LinkThought.objects.all().order_by('-posted')
    thoughts.sort(key=operator.attrgetter('posted'))
    thoughts.reverse()
    
    paginator = Paginator(thoughts, 5, orphans=2)
    p = paginator.page(page)
    
    return render_to_response('thoughts/list.html', 
        { 'thoughts': p.object_list,
          'older_page': p.next_page_number() if p.has_next() else None,
          'newer_page': p.previous_page_number() if p.has_previous() else None } )
