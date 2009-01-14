from stevelosh.thoughts.models import TextThought, LinkThought
from django.contrib import admin

class TextAdmin(admin.ModelAdmin):
    list_display = ('posted', 'title', 'body',)
    search_fields = ('title', 'body',)
    list_filter = ('posted',)
    date_hierarchy = 'posted'
    ordering = ('-posted',)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'name', 'posted', 'description',)
    search_fields = ('name', 'url', 'description',)
    list_filter = ('posted',)
    date_hierarchy = 'posted'
    ordering = ('-posted',)


admin.site.register(TextThought, TextAdmin)
admin.site.register(LinkThought, LinkAdmin)