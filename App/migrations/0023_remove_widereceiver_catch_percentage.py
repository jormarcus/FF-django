# Generated by Django 3.1 on 2020-08-23 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_remove_widereceiver_projected_catch_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widereceiver',
            name='catch_percentage',
        ),
    ]