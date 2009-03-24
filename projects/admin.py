from stevelosh.projects.models import Project, ProjectFile, Comment
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'snip', 'type', 'posted',)
    search_fields = ('name', 'snip', 'body')
    list_filter = ('type',)
    date_hierarchy = 'posted'
    ordering = ('-posted',)
    prepopulated_fields = { 'slug': ('name',) }

class ProjectFileAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'project', 'file',)
    list_display = ('project', 'title', 'description',)
    search_fields = ('title', 'description',)
    list_filter = ('project',)

class CommentAdmin(admin.ModelAdmin):
    fields = ('name', 'body', 'submitted', 'project', 'spam')
    list_display = ('project', 'name', 'submitted', 'body', 'spam')
    search_fields = ('name', 'body')
    list_filter = ('name', 'project', 'spam')
    date_hierarchy = 'submitted'
    ordering = ('-submitted',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectFile, ProjectFileAdmin)
admin.site.register(Comment, CommentAdmin)
