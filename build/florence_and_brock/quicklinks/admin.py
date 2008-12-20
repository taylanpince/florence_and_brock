from django.contrib import admin

from quicklinks.models import QuickLink


class QuickLinkModel(admin.ModelAdmin):
    list_display = ('text', 'link_preview', 'position')
    search_fields = ('text', 'link')


admin.site.register(QuickLink, QuickLinkModel)