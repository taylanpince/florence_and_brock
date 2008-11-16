from django.contrib import admin

from news.models import NewsItem
from decisions.admin import IssueInline


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pub_date', 'publication_status')
    list_filter = ('publication_status', 'author',)
    search_fields = ('title', 'teaser', 'body',)

    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'pub_date'
    inlines = (IssueInline,)


admin.site.register(NewsItem, NewsItemAdmin)

