# Generated by Django 2.0.2 on 2020-06-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='system.Menu'),
        ),
    ]
