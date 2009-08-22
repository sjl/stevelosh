from stevelosh.blog.models import Entry, Comment
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Entry', { 'fields': ['title', 'snip', 'body'], }),
        ('Publishing', { 'fields': ['pub_date', 'published'],
                         'description': "The entry won't be shown on the site unless the Published box is checked." }),
        ('Advanced', { 'fields': ['slug',],
                       'classes': ['collapse'], }),
    ]
    list_display = ('title', 'snip', 'pub_date',)
    search_fields = ('title', 'snip', 'body')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    prepopulated_fields = { 'slug': ('title',) }

class CommentAdmin(admin.ModelAdmin):
    fields = ('name', 'body', 'submitted', 'entry', 'spam')
    list_display = ('entry', 'name', 'submitted', 'snip', 'spam')
    search_fields = ('name', 'body')
    list_filter = ('name', 'entry', 'spam')
    date_hierarchy = 'submitted'
    ordering = ('-submitted',)


admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)