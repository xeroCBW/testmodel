# Generated by Django 2.2.5 on 2020-07-04 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0021_auto_20200704_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_secret',
        ),
    ]