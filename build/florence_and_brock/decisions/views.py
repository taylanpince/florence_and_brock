from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from decisions.models import Issue, Vote
from decisions.forms import IssueForm

@login_required
def issue_vote(request, issue_id):
    if not hasattr(request.user, 'unit'):
        return HttpResponseRedirect(object_url)
    issue = get_object_or_404(Issue, id=issue_id)
    object_url = issue.content_object.get_absolute_url()
    try:
        Vote.objects.get(voter=request.user, choice__issue=issue)
    except Vote.DoesNotExist:
        pass
    else:
        return HttpResponseRedirect(object_url)

    if request.method == 'POST':
        form = IssueForm(request.POST, issue=issue)
        if form.is_valid:
            vote = form.save(commit=False)
            vote.voter = request.user
            vote.save()
    return HttpResponseRedirect(object_url)
