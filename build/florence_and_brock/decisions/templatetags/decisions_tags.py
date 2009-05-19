from django import template

from decisions.forms import IssueForm
from decisions.models import Vote

register = template.Library()


@register.inclusion_tag('decisions/_issue_inline.html', takes_context=True)
def show_issue(context, issue):
    user = context.get('user', None)
    unit = getattr(user, 'unit', None)
    try:
        existing_vote = Vote.objects.get(voter__unit=unit, choice__issue=issue)
    except (KeyError, AttributeError, Vote.DoesNotExist):
        existing_vote = None

    if not existing_vote and unit is not None:
        form = IssueForm(issue=issue)
    else:
        form = None
    return {
            'issue': issue,
            'form': form,
            'existing_vote': existing_vote,
            'user': context.get('user', None),
            }