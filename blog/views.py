from stevelosh.blog.models import Entry, Comment
from markdown import markdown
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from akismet import Akismet
from stevelosh import deploy

ak = Akismet(deploy.AKISMET_API_KEY, blog_url='http://stevelosh.com/')

def entry(request, year, month, day, slug):
    entry = get_object_or_404(Entry, slug=slug, pub_date__year=year, 
                              pub_date__month=month, pub_date__day=day,)
    comments = entry.comment_set.filter(spam=False).order_by('submitted')
    
    return render_to_response('blog/entry.html', 
                              { 'entry': entry, 'comments': comments })

def old_entry(request, year, month, day, slug):
    return HttpResponsePermanentRedirect(reverse('blog-entry',
                                         args=(year, month, day, slug)))

def list(request, page=1):
    page = int(page)
    
    entries = Entry.objects.all().filter(published=True).order_by('-pub_date')
    p = Paginator(entries, 7, orphans=3).page(page)
    
    return render_to_response('blog/list.html', 
        { 'entries': p.object_list,
          'older_page': p.next_page_number() if p.has_next() else None,
          'newer_page': p.previous_page_number() if p.has_previous() else None } )

def comment(request):
    fields = request.POST
    entry = Entry.objects.get(pk=fields['entry-id'])
    
    if ( fields.has_key('name') and 
         not fields['name'].strip() == '' and
         not len(fields['name']) < 2 and
         fields.has_key('body') and 
         not fields['body'].strip() == '' and
         not len(fields['body']) < 3 and
         not len(fields['body']) > 15000):
        
        akismet_data = {}
        akismet_data['user_ip'] = request.META['REMOTE_ADDR']
        akismet_data['user_agent'] = request.META['HTTP_USER_AGENT']
        akismet_data['comment_author'] = fields['name']
        akismet_data['comment_type'] ='comment'
        spam = ak.comment_check(fields['body'].encode('ascii', 'ignore'), akismet_data)
        
        new_comment = Comment(name=fields['name'], 
                              body=fields['body'], 
                              entry=entry,
                              spam=spam)
        new_comment.save()
    
    return HttpResponseRedirect(reverse('blog-entry',
                                        args=(entry.pub_date.year, 
                                              entry.pub_date.month, 
                                              entry.pub_date.day,
                                              entry.slug)))
