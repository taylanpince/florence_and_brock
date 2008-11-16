from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from residents.forms import ResidentUserChangeForm, ResidentUserCreationForm
from residents.models import ResidentUser

class ResidentUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Housing'), {'fields': ('unit',)}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )

    form = ResidentUserChangeForm
    add_form = ResidentUserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'unit')


admin.site.register(ResidentUser, ResidentUserAdmin)
