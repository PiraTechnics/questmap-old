from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')
        parser.add_argument('-g', '--group', type=str, help='add users to group if it exists')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']
        group = kwargs['group']

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
                if group:
                    userGroup = Group.objects.get(name=group)
                    if userGroup:
                        user.groups.add(userGroup)
                        self.stdout.write('User "%s" sucessfully assigned to group "%s"!' % (user.username, group))
                    else:
                        self.stdout.write('Error: Group "%s" does not exist! Try again with a valid group' % group)