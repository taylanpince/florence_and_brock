from django.conf import settings


NEWS_PAGINATE_BY = getattr(settings, 'NEWS_PAGINATE_BY', 5)

