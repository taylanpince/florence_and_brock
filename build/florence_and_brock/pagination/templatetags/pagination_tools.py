from django import template
from django.core.exceptions import ImproperlyConfigured

from pagination.settings import PAGINATION_ON_EACH_SIDE, PAGINATION_MAX_PAGES


register = template.Library()


@register.inclusion_tag('pagination/page_controls.html', takes_context=True)
def page_controls(context, base_url=None, paginator_var='paginator', page_var='page'):
    """
    Display the pagination controls using the paginator_var (named 'paginator'
    by default) and the page_var (named 'page' by default) from the context.

    If a base_url is passed it will be used to build the URL for the other pages
    by adding a page_var querystring parameter. base_url should not contain a
    page_var query string parameter.

    If no base_url is passed and the request is available in the context, it
    will be used.

    This is needed if the request already contains a querystring parameter (a
    sort parameter for instance).

    Usage::

        {% page_controls %}
        {% page_controls 'http://host/path/?id=3' 'paginator' 'page' %}
    """
    # MEDIA_URL is used if one wants to supply graphical navigation links
    MEDIA_URL = context.get('MEDIA_URL', None)
    paginator = context.get(paginator_var, None)
    page_obj = context.get('page_obj', None)
    if paginator:
        page_num = context.get(page_var, 1)
        if not page_obj:
            try:
                page_obj = paginator.page(page_num)
            except InvalidPage:
                pass
    if base_url:
        if '?' in base_url:
            base_url += '&'
        else:
            base_url += '?'
    else:
        request = context.get('request', None)
        if request is None:
            raise ImproperlyConfigured("The request context processor is needed by the page_controls templatetag")
        base_url = request.path + '?'
        querydict = request.GET.copy()
        if page_var in querydict:
            del querydict[page_var]
        if len(querydict) > 0: # There is others querystring parameters
            base_url += querydict.urlencode() + '&'

    if page_obj and page_obj.has_other_pages:
        # If there are MAX_PAGES or fewer pages, display links to every page.
        # Otherwise, do some fancy
        ON_EACH_SIDE = PAGINATION_ON_EACH_SIDE
        MAX_PAGES = PAGINATION_MAX_PAGES
        DOT = '.'

        if paginator.num_pages <= MAX_PAGES:
            page_range = paginator.page_range
        else:
            # Insert "smart" pagination links, so that there are always
            # ON_EACH_SIDE * 2 pagination links.
            page_range = []
            if page_num > (ON_EACH_SIDE + 3):
                page_range.append(1)
                page_range.append(DOT)
                page_range.extend(range(
                    min(paginator.num_pages - 3, page_num) - ON_EACH_SIDE,
                    min(paginator.num_pages, page_num + ON_EACH_SIDE) + 1))
            else:
                page_range.extend(range(1, ON_EACH_SIDE * 2 + 3))

            if page_num < (paginator.num_pages - ON_EACH_SIDE - 2):
                page_range.append(DOT)
                page_range.append(paginator.num_pages)
            else:
                page_range.extend(range(page_range[-1] + 1,
                    min(paginator.num_pages, page_range[-1] + ON_EACH_SIDE) + 1))

    return locals()
