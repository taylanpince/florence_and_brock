from django.views.generic import list_detail
from django.conf import settings

from pagination.tests.models import TestModel


def testmodel_list(request):
    qs = TestModel.objects.all()
    return list_detail.object_list(request, qs, paginate_by=settings.PAGINATE_BY)
