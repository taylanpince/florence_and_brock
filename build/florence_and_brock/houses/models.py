from django.db import models
from django.utils.translation import ugettext_lazy as _


class HousingUnit(models.Model):
    """A housing unit in the complex"""
    address = models.CharField(_('address'), blank=True, max_length=100)

    class Meta:
        verbose_name = _('housing unit')
        verbose_name_plural = _('housing units')
        ordering = ('address',)

    def __unicode__(self):
        return self.address
