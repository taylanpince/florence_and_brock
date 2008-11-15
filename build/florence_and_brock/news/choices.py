from django.utils.translation import ugettext_lazy as _

HOME_PAGE = 0
NEWS_LISTING = 1
ARCHIVE_ONLY = 2

PUBLICATION_STATUS = (
        (HOME_PAGE, _('home page')),
        (NEWS_LISTING, _('news listing')),
        (ARCHIVE_ONLY, _('archive only')),
        )

