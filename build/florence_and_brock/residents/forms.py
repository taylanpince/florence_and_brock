from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from residents.models import ResidentUser

class ResidentUserChangeForm(UserChangeForm):
    class Meta:
        model = ResidentUser


class ResidentUserCreationForm(UserCreationForm):
    class Meta:
        model = ResidentUser
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            ResidentUser.objects.get(username=username)
        except ResidentUser.DoesNotExist:
            return username
        raise forms.ValidationError(_("A user with that username already exists."))
