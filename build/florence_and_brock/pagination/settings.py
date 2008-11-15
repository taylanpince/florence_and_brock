from django.conf import settings

PAGINATION_ON_EACH_SIDE = getattr(settings, 'PAGINATION_ON_EACH_SIDE', 2)

PAGINATION_MAX_PAGES = getattr(settings, 'PAGINATION_MAX_PAGES', 10)



