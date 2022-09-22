from django.core.management.base import BaseCommand, CommandError
from uptimebot.handler import remove_expired_uptimes

class Command(BaseCommand):
    help = 'Removed expired uptimes'

    def handle(self, *args, **options):
        remove_expired_uptimes()