from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from maps import models

GROUPS = {
    "Game Master": {
        models.Campaign: ['add', 'change', 'delete', 'view'],
        models.Map: ['add', 'change', 'delete', 'view'],
        models.Location: ['add', 'change', 'delete', 'view'],
        models.Character: ['add', 'change', 'delete', 'view'],
        models.Note: ['add', 'change', 'delete', 'view'],
    },

    "Player": {
        models.Campaign: ['view'],
        models.Map: ['view'],
        models.Location: ['view'],
        models.Character: ['add', 'change', 'delete', 'view'],
        models.Note: ['add', 'change', 'delete', 'view'],
    },
}

class Command(BaseCommand):
    help = 'Create basic app groups with relevant permissions. You should only need to run this when deploying app, or upon DB reinstancing.'

    def handle(self, *args, **kwargs):

        for group_name in GROUPS:
            new_group, _ = Group.objects.get_or_create(name=group_name)
            # Loop thru models in current group
            for app_model in GROUPS[group_name]:
                #Loop permissions in Group/Model
                for permission_name in GROUPS[group_name][app_model]:
                    # Generate permission name, Django-Style, for each
                    name = "Can {} {}".format(permission_name, app_model.__name__.lower())
                    print("Creating {}".format(name))

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        self.stdout.write("Permission not found with name '{}'.".format(name))
                        continue

                    new_group.permissions.add(model_add_perm)