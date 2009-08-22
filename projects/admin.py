from stevelosh.projects.models import Project, Comment
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'snip', 'type', 'posted',)
    search_fields = ('name', 'snip', 'body')
    list_filter = ('type',)
    date_hierarchy = 'posted'
    ordering = ('-posted',)
    prepopulated_fields = { 'slug': ('name',) }

class CommentAdmin(admin.ModelAdmin):
    fields = ('name', 'body', 'submitted', 'project', 'spam')
    list_display = ('project', 'name', 'submitted', 'snip', 'spam')
    search_fields = ('name', 'body')
    list_filter = ('name', 'project', 'spam')
    date_hierarchy = 'submitted'
    ordering = ('-submitted',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment, CommentAdmin)
