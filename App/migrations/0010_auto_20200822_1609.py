# Generated by Django 3.1 on 2020-08-22 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20200822_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quarterback',
            old_name='Name',
            new_name='player_name',
        ),
        migrations.RenameField(
            model_name='quarterback',
            old_name='Position',
            new_name='player_position',
        ),
    ]
