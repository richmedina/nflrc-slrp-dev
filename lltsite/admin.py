# lltsite/admin.py
from django.contrib import admin

from .models import StoryPage, Dissertation


class StoryPageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'featured', 'get_absolute_url')
    list_display_links = ('pk',)

class DissertationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')


admin.site.register(StoryPage, StoryPageAdmin)
admin.site.register(Dissertation, DissertationAdmin)
