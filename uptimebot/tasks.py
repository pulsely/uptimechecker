# Celery Tasks for uptimebot
import colorama

from uptimechecker.celery import app
from celery.schedules import crontab
from celery.utils.log import get_task_logger
# from celery import shared_task
from django.utils import timezone
from django.conf import settings
from uptimebot.handler import check_domains

logger = get_task_logger(__name__)


# @app.on_after_configure.connect
# @app.on_after_finalize.connect
#
# def setup_periodic_tasks(sender, **kwargs):
#     # # Calls test('hello') every 10 seconds.
#     # sender.add_periodic_task(60.0, test.s('hello'), name='add every 10')
#     #
#     # # Calls test('world') every 30 seconds
#     sender.add_periodic_task(3.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(minute=1),
#         test.s('Happy Mondays!'),
#     )
#
#

# Schedule
# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     if settings.DEBUG:
#         print(
#             f"{colorama.Fore.GREEN}DEFAULT_PERIODIC_MINUTES: {colorama.Style.RESET_ALL}{settings.DEFAULT_PERIODIC_MINUTES}")
#
#     sender.add_periodic_task(
#         crontab(minute=f'*/1'),
#         check_domains(),
#         expires=60
#     )
#
#     # sender.add_periodic_task(
#     #     crontab(minute=f'*/1'),
#     #     test.s('triggered'), expires=86400
#     # )
#     #
#     # sender.add_periodic_task(
#     #     crontab(minute=f'*/{settings.DEFAULT_PERIODIC_MINUTES}'),
#     #     check_domains(),
#     #     expires=86400
#     # )
#     #sender.add_periodic_task(3.0, test.s('world'), expires=10)

@app.task
def test(arg):
    print( f"{arg} at %s" % timezone.now() )

    check_domains()