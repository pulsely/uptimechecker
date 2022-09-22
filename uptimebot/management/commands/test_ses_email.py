from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Send a test e-mail(s) with SES'

    def add_arguments(self, parser):
        parser.add_argument('emails', nargs='+', type=str)

    def handle(self, *args, **options):
        print(">> triggered SES")
        for email in options['emails']:
            print(email)

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
