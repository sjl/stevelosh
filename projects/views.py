from stevelosh.projects.models import Project, Comment
from markdown import markdown
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    comments = project.comment_set.filter(spam=False).order_by('submitted')
    
    return render_to_response('projects/project.html', 
                              { 'project': project, 'comments': comments })

def list(request):
    projects = Project.objects.all().order_by('-posted')
    return render_to_response('projects/list.html', { 'projects': projects, })

def comment(request):
    fields = request.POST
    project = Project.objects.get(pk=fields['project-id'])
    
    if ( fields.has_key('name') and 
         not fields['name'].strip() == '' and
         not len(fields['name']) < 3 and
         fields.has_key('body') and 
         not fields['body'].strip() == '' and
         not len(fields['body']) < 3 and
         not len(fields['body']) > 15000):
        new_comment = Comment(name=fields['name'], 
                              body=fields['body'], 
                              project=project)
        new_comment.save()
    
    return HttpResponseRedirect(reverse('stevelosh.projects.views.project',
                                        args=(project.slug,)))