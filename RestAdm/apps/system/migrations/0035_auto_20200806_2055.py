# Generated by Django 2.2.5 on 2020-08-06 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0034_auto_20200806_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='button',
            old_name='url',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='code',
            new_name='url',
        ),
    ]
