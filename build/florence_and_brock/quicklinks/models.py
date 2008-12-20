# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class QuickLink(models.Model):
    """A quick link to feature in the Quick Links sidebar box"""
    text = models.CharField(_('text'), max_length=100)
    link = models.URLField(_('link'), verify_exists=False)
    position = models.IntegerField(_('position'), blank=True, null=True,
                                   help_text=_('The position of this link '
                                               'relative to the other links. '
                                               'List is sorted from low to high.'))

    class Meta:
        verbose_name = _('quicklink')
        verbose_name_plural = _('quicklinks')
        ordering = ('position',)

    def __unicode__(self):
        return self.text

    def link_preview(self):
        preview = self.link[:50]
        if len(self.link) > 50:
            preview += u'…'
        return preview