from stevelosh.blog.models import Entry, Comment
from markdown import markdown
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse


ENTRIES_PER_PAGE = 10

def entry(request, year, month, day, slug):
    entry = get_object_or_404(Entry, slug=slug, pub_date__year=year, 
                              pub_date__month=month, pub_date__day=day,)
    return render_to_response('blog/entry.html', { 'entry': entry, })

def old_entry(request, year, month, day, slug):
    return HttpResponsePermanentRedirect(reverse('blog-entry',
                                         args=(year, month, day, slug)))

def list(request, page=0):
    page = int(page)
    start_index = page * ENTRIES_PER_PAGE
    end_index = start_index + ENTRIES_PER_PAGE
    entries = Entry.objects.all().order_by('-pub_date')
    entries = entries.filter(published=True)[start_index:end_index]
    return render_to_response('blog/list.html', 
        { 'entries': entries,
          'older_page': page+1 if end_index < Entry.objects.count() else None,
          'newer_page': page-1 if page != 0 else None } )

def comment(request):
    fields = request.POST
    entry = Entry.objects.get(pk=fields['entry-id'])
    
    if ( fields.has_key('name') and (not fields['name'].strip() == '') and
         fields.has_key('body') and not fields['body'].strip() == ''):
        new_comment = Comment(name=fields['name'], 
                              body=fields['body'], 
                              entry=entry)
        new_comment.save()
    
    return HttpResponseRedirect(reverse('stevelosh.blog.views.entry',
                                        args=(entry.pub_date.year, 
                                              entry.pub_date.month, 
                                              entry.pub_date.day,
                                              entry.slug)))
