from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from django.core.mail import send_mail
from django.conf import settings
import colorama
from django.utils import timezone

class Command(BaseCommand):
    help = 'Send a test e-mail(s) with SES'

    def add_arguments(self, parser):
        parser.add_argument('emails', nargs='+', type=str)

    def handle(self, *args, **options):
        if settings.SERVER_EMAIL:
            print(f"{colorama.Fore.GREEN}>> Triggered Django e-mail test{colorama.Style.RESET_ALL}")
            for email in options['emails']:
                print(email)

                try:
                    send_mail(
                        "Test e-mail from Uptime Checker",
                        "Test e-mail generated on %s" % timezone.now(),
                        settings.SERVER_EMAIL,
                        options['emails'],
                        fail_silently=False,
                    )
                except Exception as e:
                    print(f"{colorama.Fore.RED}Error: {colorama.Style.RESET_ALL} {e}")
        else:
            print(f"{colorama.Fore.RED}Sorry, you have not setup the SERVER_EMAIL in the .env file.")
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
