from django.contrib.auth.decorators import login_required
from django.views.generic import list_detail

from residents.models import ResidentUser

@login_required
def contact_list(request):
    contacts = ResidentUser.objects.order_by('unit')
    return list_detail.object_list(
        request, contacts,
        template_object_name='contact',
        template_name='residents/contact_list.html')