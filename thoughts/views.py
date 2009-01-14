from stevelosh.thoughts.models import TextThought, LinkThought
from django.shortcuts import render_to_response
import operator

ENTRIES_PER_PAGE = 10

def list(request, page=0):
    page = int(page)
    start_index = page * ENTRIES_PER_PAGE
    end_index = start_index + ENTRIES_PER_PAGE
    total_count = TextThought.objects.count() + LinkThought.objects.count()
    
    thoughts = []
    thoughts += TextThought.objects.all().order_by('-posted')
    thoughts += LinkThought.objects.all().order_by('-posted')
    thoughts.sort(key=operator.attrgetter('posted'))
    thoughts.reverse()
    thoughts = thoughts[start_index:end_index]
    
    return render_to_response('thoughts/list.html', 
        { 'thoughts': thoughts,
          'older_page': page+1 if end_index < total_count else None,
          'newer_page': page-1 if page != 0 else None } )
