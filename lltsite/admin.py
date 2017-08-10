# lltsite/admin.py
from django.contrib import admin

from .models import StoryPage

class ExtraMedia:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]

class StoryPageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'featured', 'get_absolute_url')
    list_display_links = ('pk',)

admin.site.register(StoryPage, StoryPageAdmin, Media = ExtraMedia)
