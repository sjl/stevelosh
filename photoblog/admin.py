from stevelosh.photoblog.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Entry', { 'fields': ['title', 'original_image', 'body'] }),
        ('Publishing', { 'fields': ['pub_date', 'published'] }),
        ('Advanced', { 'fields': ['slug'] }),
    ]
    save_on_top = True
    list_display = ('title', 'snippet', 'num_views', 'pub_date', 'published',)
    list_filter = ('published',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    prepopulated_fields = { 'slug': ('title',) }

admin.site.register(Entry, EntryAdmin)
