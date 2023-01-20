from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create a set of mock data for testing'

    """
    1 Superuser
    x 'GM' Users
    y 'Player' Users

    x Campaigns
    y maps
    z notes
    a characters

    """

    def add_arguments(self, parser):
        #parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        #parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        #parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')
        parser.add_argument('-u', '--users', type=int, help='Indicates the number of users to be created')

        # How much of each type of data should we generate?
        # We need to create a number of GM and player users, and should create varied but appropriate datasets for each...

        parser.add_argument('-c', '--campaigns', type=int, help='Indicates the number of campaigns to be created for each user')
        

    def handle(self, *args, **kwargs):
       map_title = "blah"

       """
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string(6))
            else:
                username = get_random_string(6)

            if admin:
                user = User.objects.create_superuser(username=username, email='', password='123')
                self.stdout.write('Superuser "%s (id: %s)" sucessfully created!' % (user.username, user.id))
            else:
                user = User.objects.create_user(username=username, email='', password='123')
                self.stdout.write('User "%s (id: %s)" sucessfully created!' % (user.username, user.id))
        """