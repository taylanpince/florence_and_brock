from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import simple, list_detail
from django.shortcuts import get_object_or_404

from news.models import NewsItem
from news.settings import NEWS_PAGINATE_BY


def home(request):
    newsitem = NewsItem.home_objects.all()[0]
    if request.user.is_authenticated():
        return simple.direct_to_template(request,
                template="news/home.html",
                extra_context=locals())
    else:
        return simple.direct_to_template(request,
                template="registration/login.html",
                extra_context=locals())


def home_login(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/')
    return login(request)


def home_logout(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/')
    return logout(request, '/')


@login_required
def newsitem_list(request):
    qs = NewsItem.objects.all()
    return list_detail.object_list(request, qs,
            paginate_by=NEWS_PAGINATE_BY,
            template_name='news/newsitem_list.html',
            template_object_name='newsitem',
            )


@login_required
def newsitem_archive(request):
    qs = NewsItem.archive_objects.all()
    return list_detail.object_list(request, qs,
            paginate_by=NEWS_PAGINATE_BY,
            template_name='news/newsitem_archive.html',
            template_object_name='newsitem',
            )


@login_required
def detail(request, year, month, slug):
    year = int(year)
    month = int(month)
    newsitem = get_object_or_404(
        NewsItem.objects,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug)

    return simple.direct_to_template(request,
            template="news/newsitem_detail.html",
            extra_context=locals())



