# Generated by Django 3.1 on 2020-08-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_auto_20200823_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarterback',
            name='Bye_Week',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
