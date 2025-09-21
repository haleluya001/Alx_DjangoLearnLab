from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'bookshelf':
        Book = apps.get_model('bookshelf', 'Book')

        # Create groups
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Fetch permissions
        perms = Permission.objects.filter(content_type__app_label='bookshelf', codename__in=[
            'can_view', 'can_create', 'can_edit', 'can_delete'
        ])
        perm_map = {p.codename: p for p in perms}

        # Assign permissions
        viewers.permissions.set([perm_map['can_view']])
        editors.permissions.set([perm_map['can_view'], perm_map['can_create'], perm_map['can_edit']])
        admins.permissions.set([perm_map['can_view'], perm_map['can_create'], perm_map['can_edit'], perm_map['can_delete']])
