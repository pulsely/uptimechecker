

from django import forms
import re, datetime
from django.forms import widgets
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.conf import settings
from uptimecheckcore import models

class AddUserForm(forms.Form):
    first_name =  forms.CharField()
    last_name =  forms.CharField()
    username =  forms.EmailField()
    role = forms.CharField()

class DeleteUserForm(forms.Form):
    user_id = forms.IntegerField()