# Generated by Django 2.0.2 on 2020-06-27 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0018_auto_20200627_1449'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('good', 'user')},
        ),
    ]
