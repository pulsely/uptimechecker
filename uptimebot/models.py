from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class TargetWebsite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    url = models.CharField( max_length=400, help_text="URL of website to check" )

    must_contain_keyword = models.CharField( max_length=400, null=True, blank=True, help_text="Keyword to check for successful" )
    flag_cdn_random_key = models.BooleanField( default=True, help_text="Add random GET parameter for proxy" )
    flag_check_ssl_expire_time = models.BooleanField("Check SSL Expire Time", default=True, help_text="Check SSL expiration?")
    ssl_expire_time = models.DateTimeField(null=True, blank=True, help_text="Current SSL expiration time")

    flag_notify_downtime = models.BooleanField(default=True)

    creation_date = models.DateTimeField("Creation date", editable=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.url}"

    class Meta:
        ordering = ('url',)
        managed = True

        verbose_name = 'Target Website'
        verbose_name_plural = 'Target Websites'


class UptimeCheck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    STATUS_CHOICES = (
        ('checking', '0: Checking'),
        ('normal', '1: Normal'),
        ('error', '2: Error'),
        ('exception', '3: Exception'),
        ('missing_keyword', '4: Missing Keyword')
    )

    url = models.CharField(max_length=400)
    target_website = models.ForeignKey( TargetWebsite, on_delete=models.CASCADE )

    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, null=True, blank=True, max_length=200)

    error_description = models.TextField( null=True, blank=True )

    payload = models.JSONField("Payload", null=True, blank=True)

    def badge_color(self):
        if self.status == 'normal':
            return "badge-success"
        else:
            return "badge-danger"

    def __str__(self):
        return f"{self.url} {self.start_time}"

    class Meta:
        ordering = ('-start_time',)
        managed = True

        verbose_name = 'Uptime Check'
        verbose_name_plural = 'Uptime Checks'
