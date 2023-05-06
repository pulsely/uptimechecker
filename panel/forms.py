

from django import forms
import re, datetime
from django.forms import widgets
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.conf import settings
from uptimecheckcore import models
from django.contrib.auth.password_validation import validate_password

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