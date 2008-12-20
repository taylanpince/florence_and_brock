from django.conf import settings

DEFAULT_MAX_QUICKLINKS = 12

MAX_QUICKLINKS = getattr(settings, 'MAX_QUICKLINKS', DEFAULT_MAX_QUICKLINKS)