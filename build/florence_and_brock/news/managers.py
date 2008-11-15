from datetime import datetime

from django.db import models

from news.choices import *


class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(
                pub_date__lt=datetime.now())


class HomePageManager(PublishedManager):
    def get_query_set(self):
        return super(HomePageManager, self).get_query_set().filter(
                publication_status=HOME_PAGE)


class NewsListingManager(PublishedManager):
    def get_query_set(self):
        return super(NewsListingManager, self).get_query_set().filter(
                models.Q(publication_status=HOME_PAGE) | \
                models.Q(publication_status=NEWS_LISTING))


