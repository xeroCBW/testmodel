# Generated by Django 2.2.5 on 2020-08-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0040_auto_20200809_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='电话'),
        ),
    ]
