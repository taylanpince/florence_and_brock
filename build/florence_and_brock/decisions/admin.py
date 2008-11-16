from django.contrib import admin
from django.contrib.contenttypes import generic

from decisions.models import Issue, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice


class IssueAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('name', 'creation_date')
    search_filter = ('name', 'description')
    inlines = (ChoiceInline,)

admin.site.register(Issue, IssueAdmin)


class IssueInline(generic.GenericStackedInline):
    model = Issue
    max_num = 1
    extra = 1

