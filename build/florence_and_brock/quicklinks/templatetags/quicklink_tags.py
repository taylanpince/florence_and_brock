from django import template

from quicklinks.models import QuickLink
from quicklinks import settings

register = template.Library()


@register.inclusion_tag('quicklinks/_quicklink_list.html')
def show_quicklinks():
    return {'quicklink_list': QuickLink.objects.all()[:settings.MAX_QUICKLINKS]}