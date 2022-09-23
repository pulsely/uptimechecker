import os

import colorama
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uptimechecker.settings')

app = Celery('uptimechecker')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

from django.conf import settings

if settings.DEBUG:
    print(f"{colorama.Fore.GREEN}Setting DEFAULT_PERIODIC_MINUTES for cronjob: {colorama.Fore.RED}{settings.DEFAULT_PERIODIC_MINUTES}{colorama.Style.RESET_ALL}")
app.conf.beat_schedule = {
 # Executes every Monday morning at 7:30 a.m.
 "add-every-monday-morning": {
     "task": "uptimebot.tasks.test",
     "schedule": crontab(minute=f'*/{settings.DEFAULT_PERIODIC_MINUTES}'),
     "args": (16,),
 },
}