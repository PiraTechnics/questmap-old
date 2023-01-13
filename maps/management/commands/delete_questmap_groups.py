from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Delete all User Groups'

    def handle(self, *args, **kwargs):
        groups = Group.objects.all()
        for group in groups:
            group.delete()
        self.stdout.write("All User Groups Deleted")