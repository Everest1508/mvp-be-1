from django.core.management.base import BaseCommand
from user_log.models import College, Games, SubEvents, MainEvent,User
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate dummy data for models'

    def handle(self, *args, **kwargs):
        # Create users
        sub_event1 = SubEvents.objects.create(
            title='Soccer Tournament',
            game=game1,
            description='Join our exciting soccer tournament! Show off your skills on the field.',
            rules='1. Each team must have a minimum of 5 players.\n2. Matches will be played in a knockout format.',
        )

        sub_event2 = SubEvents.objects.create(
            title='Chess Championship',
            game=game2,
            description='Participate in the ultimate chess championship. Test your strategic thinking against the best!',
            rules='1. Each player must be familiar with standard chess rules.\n2. Rounds will follow a Swiss-system format.',
        )

        # Create main event
        main_event = MainEvent.objects.create(
            title='Main Event 2024',
        )

        # Add sub events to main event
        main_event.sub_events.add(sub_event1, sub_event2)

        self.stdout.write(self.style.SUCCESS('Dummy data populated successfully.'))
