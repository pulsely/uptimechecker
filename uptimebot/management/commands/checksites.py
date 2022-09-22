from django.core.management.base import BaseCommand, CommandError
from uptimebot.handler import check_domains

class Command(BaseCommand):
    help = 'Trigger uptime checks for all websites'

    def handle(self, *args, **options):
        check_domains()