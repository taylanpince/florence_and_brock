from django import forms
from django.utils.translation import ugettext_lazy as _

from decisions.models import Choice, Vote


class IssueChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.text

class IssueForm(forms.ModelForm):
    choice = IssueChoiceField(
                label=_('Choices'),
                empty_label=None,
                queryset=Choice.objects.all(),
                widget=forms.RadioSelect())

    class Meta:
        model = Vote
        fields = ('choice',)

    def __init__(self, *args, **kwargs):
        self.issue = kwargs.pop('issue')
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice.objects.filter(issue=self.issue)
