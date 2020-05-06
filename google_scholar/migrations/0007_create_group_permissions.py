from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    author_permissions = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                             content_type__model='author')

    article_permissions = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                          content_type__model='article')

    topic_permissions = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                                  content_type__model='topic')

    journal_permissions = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                                  content_type__model='journal')


    perm_view_author = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                           content_type__model='author',
                                                           codename='view_author')

    perm_view_article = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                        content_type__model='article',
                                                        codename='view_article')

    perm_view_topic = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                               content_type__model='topic',
                                                               codename='view_topic')

    perm_view_journal = permission_class.objects.filter(content_type__app_label='google_scholar',
                                                               content_type__model='journal',
                                                               codename='view_journal')



    viewer_permissions = chain(perm_view_article)

    sys_admin_permissions = chain(author_permissions,
                                  topic_permissions,
                                  journal_permissions,
                                  perm_view_author,
                                  perm_view_article,
                                  perm_view_topic,
                                  perm_view_journal
                                    )

    sys_registrar_permissions = chain(
                                     article_permissions,
                                     perm_view_author,
                                     perm_view_article,
                                     perm_view_topic,
                                     perm_view_journal)

    my_groups_initialization_list = [
        {
            "name": "viewer",
            "permissions_list": viewer_permissions,
        },
        {
            "name": "sys_admin",
            "permissions_list": sys_admin_permissions,
        },
        {
            "name": "sys_registrar",
            "permissions_list": sys_registrar_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('google_scholar', '0006_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
