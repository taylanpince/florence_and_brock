import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Issue(models.Model):
    """An issue for which each housing unit has a vote."""
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateTimeField(_('creation date'), default=datetime.datetime.now)

    class Meta:
        verbose_name = _('issue')
        verbose_name_plural = _('issues')

    def __unicode__(self):
        return self.name


class Choice(models.Model):
    """A choice that a housing unit can vote on in an issue"""
    issue = models.ForeignKey(Issue, verbose_name=_('issue'))
    text = models.CharField(_('text'), max_length=200)
    number = models.IntegerField(_('number'), default=1,
        help_text=_('The position of the choice in the list of choices for the issue'))

    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choices')
        ordering = ('number',)

    def __unicode__(self):
        return _('%(issue)s choice #%(number)s: %(choice_text)s)') % {
            'issue': self.issue,
            'number': self.number,
            'choice_text': self.text
            }


class Vote(models.Model):
    """A vote on an issue"""
    choice = models.ForeignKey(Choice, verbose_name=_('choice'))
    voter = models.ForeignKey('residents.ResidentUser', verbose_name=_('voter'))

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')

    def __unicode__(self):
        return _('%(unit)s voted "%(choice)s" on %(issue)s') % {
            'unit': self.voter.unit,
            'choice': self.choice,
            'issue': self.choice.issue.name
        }

    def save(self):
        try:
            Vote.objects.get(choice__issue=self.choice.issue, voter__unit=self.voter.unit)
        except Vote.DoesNotExist:
            pass
        else:
            raise ValidationError(_('The unit %(unit)s has already voted on issue %(issue)s') % {
                'unit': self.voter.unit,
                'issue': self.choice.issue,
            })