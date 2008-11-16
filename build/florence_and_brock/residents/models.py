from django.contrib.auth.models import User, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ResidentUser(User):
    """User living in a housing unit."""
    unit = models.ForeignKey('houses.HousingUnit', null=True, blank=True, verbose_name=_('unit'))
    phone = models.CharField(_('phone'), blank=True, max_length=100)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()