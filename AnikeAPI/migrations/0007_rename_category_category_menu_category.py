# Generated by Django 4.2.1 on 2023-05-27 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnikeAPI', '0006_rename_category_id_menuitem_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='menu_category',
        ),
    ]
