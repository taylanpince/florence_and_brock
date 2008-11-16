from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from news.choices import PUBLICATION_STATUS, NEWS_LISTING
from news.managers import PublishedManager, HomePageManager, NewsListingManager
from decisions.models import Issue


class NewsItem(models.Model):
    publication_status = models.PositiveSmallIntegerField(_('publication status'),
            choices=PUBLICATION_STATUS, default=NEWS_LISTING)
    pub_date = models.DateTimeField(_('publication date'), default=datetime.now)
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(max_length=100, unique_for_month="pub_date")
    teaser = models.TextField(_('teaser'))
    body = models.TextField(_('body'))
    image = models.ImageField(_('image'), upload_to='files/news/images',
            blank=True)
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    documents = models.ManyToManyField('documents.Document',
            verbose_name=_('documents'), blank=True)

    admin_objects = models.Manager()
    objects = NewsListingManager()
    home_objects = HomePageManager()
    archive_objects = PublishedManager()

    class Meta:
        verbose_name = _('news item')
        verbose_name_plural = _('news items')
        ordering = ('-pub_date', '-id', )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('newsitem_detail', None, {
                'year': self.pub_date.year,
                'month': self.pub_date.strftime('%m'),
                'slug': self.slug })

    def get_issues(self):
        ct = ContentType.objects.get_for_model(self)
        return Issue.objects.filter(content_type=ct, object_id=self.id)
