from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model

from residents.models import ResidentUser

class ResidentUserBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        user = super(ResidentUserBackend, self).authenticate(username, password)
        try:
            return user.residentuser
        except (AttributeError, ResidentUser.DoesNotExist):
            return user

    def get_user(self, user_id):
        user = super(ResidentUserBackend, self).get_user(user_id)
        try:
            return user.residentuser
        except (AttributeError, ResidentUser.DoesNotExist):
            return user
