from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string

from residents.models import ResidentUser


def handle_news_save(sender, instance=None, created=False, **kwargs):
    if created:
        site = Site.objects.get_current()
        for user in ResidentUser.objects.exclude(email=''):
            context = {'site': site, 'user': user, 'news_item': instance}
            subject = 'New on %s: %s' % (site.name, instance.title)
            message = render_to_string('news/news_notify_email.txt', context)
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
