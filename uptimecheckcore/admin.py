from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from . import models


# Register your models here.
class CustomUserAdmin(UserAdmin):
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (_('Personal info'), {'fields': (('first_name', 'last_name'), ('email', 'role'),)}),
    #
    #     (_('ID Information'), {'fields': (('payload', 'role'),)}),
    #
    #     # Django Admin stuff go to below
    #
    #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    #     (_('Important dates'), {'fields': (('last_login', 'date_joined'),)}),
    #
    # )
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'role',)


admin.site.register(models.User, CustomUserAdmin)
