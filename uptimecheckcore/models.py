from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default='client')

    AUTH_TYPE = (
        ('system', 'System'),
        ('firebase', 'Firebase'),
    )
    auth_type = models.CharField(max_length=20, choices=AUTH_TYPE, default='system')
