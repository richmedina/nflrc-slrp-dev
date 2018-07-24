# lltsite/admin.py
from django.contrib import admin

from .models import StoryPage, Subscriber, ImpactFactor

class ExtraMedia:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]

class StoryPageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'featured', 'get_absolute_url', 'slug')
    list_editable = ('slug',)
    list_display_links = ('pk',)

admin.site.register(StoryPage, StoryPageAdmin, Media = ExtraMedia)
admin.site.register(Subscriber)
admin.site.register(ImpactFactor)
