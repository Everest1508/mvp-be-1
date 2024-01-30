# yourapp/management/commands/update_participation.py
from django.core.management.base import BaseCommand
from user_log.models import User, SubEvents

class Command(BaseCommand):
    help = 'Update participated_events field for all users based on their actual participation'

    def handle(self, *args, **options):
        self.stdout.write('Updating participated_events for all users...')

        # Iterate through all sub-events
        for sub_event in SubEvents.objects.all():
            self.update_participation_for_sub_event(sub_event)

        self.stdout.write(self.style.SUCCESS('Participation update complete'))

    def update_participation_for_sub_event(self, sub_event):
        # Get the list of user IDs currently participating in the sub-event
        current_participation = [str(user.id) for user in sub_event.participants.all()]

        # Iterate through all users
        for user in User.objects.all():
            self.update_user_participation(user, sub_event, current_participation)

    def update_user_participation(self, user, sub_event, current_participation):
        user_id_str = str(user.id)

        if user_id_str in current_participation:
            # User is already participating, nothing to change
            pass
        else:
            # User is not participating, update the participated_events field
            user.participated_events = self.remove_event_id(user.participated_event, str(sub_event.id))
            user.save()

        self.stdout.write(self.style.SUCCESS(f'Updated participation for user {user.name} in sub-event {sub_event.title}'))

    def remove_event_id(self, participated_events, event_id):
        # Helper method to remove event_id from participated_events
        events_list = []
        try:
            events_list = [e.strip() for e in participated_events.split(',') if e]
            events_list = [e for e in events_list if e != event_id]
        except:
            pass
        return ','.join(events_list)
