# Generated by Django 2.0.2 on 2020-06-24 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='role',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='structure',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_delete',
        ),
    ]
