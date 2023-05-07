

from django import forms
import re, datetime
from django.forms import widgets
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.conf import settings
from uptimecheckcore import models
from django.contrib.auth.password_validation import validate_password

# For resetting the password with Django Management Command "reset"
class AdminResetForm(forms.Form):
    password = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])


# Users
class EditUserForm(forms.Form):
    id = forms.CharField(required=False)
    operation = forms.CharField() # either "create" or "edit"
    first_name =  forms.CharField()
    last_name =  forms.CharField()
    username =  forms.CharField()
    email =  forms.EmailField()

    role = forms.CharField()

class AddUserForm(EditUserForm):
    password = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])

class DeleteUserForm(forms.Form):
    user_id = forms.IntegerField()

class ReadUserForm(forms.Form):
    user_id = forms.IntegerField()

class ResetPasswordForm(forms.Form):
    user_id = forms.IntegerField()
    new_password = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])
    new_password = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])

# Websites

class EditWebsiteForm(forms.Form):
    id = forms.CharField(required=False)
    title = forms.CharField()  # either "create" or "edit"
    url = forms.URLField()
    must_contain_keyword = forms.CharField(required=False)
    flag_cdn_random_key = forms.BooleanField(required=False)
    flag_check_ssl_expire_time = forms.BooleanField(required=False)
    flag_notify_downtime = forms.BooleanField(required=False)

    operation = forms.CharField()


class DeleteWebsiteForm(forms.Form):
    website_id = forms.CharField()

class ReadWebsiteForm(forms.Form):
    website_id = forms.UUIDField()
