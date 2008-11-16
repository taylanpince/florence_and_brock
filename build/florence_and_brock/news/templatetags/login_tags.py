from django import template
from django.contrib.auth.forms import AuthenticationForm

register = template.Library()


@register.inclusion_tag('_login_form.html')
def login_form():
    form = AuthenticationForm()
    return {'form': form}
