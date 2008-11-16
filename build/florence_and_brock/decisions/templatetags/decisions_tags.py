from django import template

from decisions.forms import IssueForm
from decisions.models import Vote

register = template.Library()


@register.inclusion_tag('decisions/_issue_inline.html', takes_context=True)
def show_issue(context, issue):
    user = context.get('user', None)
    unit = getattr(user, 'unit', None)
    try:
        unit_voter = Vote.objects.get(voter__unit=unit, choice__issue=issue).voter
    except (KeyError, AttributeError, Vote.DoesNotExist):
        unit_voter = None

    form = IssueForm(issue=issue)
    return {
            'issue': issue,
            'form': form,
            'unit_voter': unit_voter,
            'user': context.get('user', None),
            'can_vote': unit != None}