# Generated by Django 3.1 on 2020-08-23 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_auto_20200822_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quarterback',
            old_name='pos',
            new_name='position',
        ),
    ]
