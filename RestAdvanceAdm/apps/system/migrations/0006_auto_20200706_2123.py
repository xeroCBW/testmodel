# Generated by Django 2.2.5 on 2020-07-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20200706_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='actionsOption',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='check_all',
        ),
        migrations.AlterField(
            model_name='permission',
            name='type',
            field=models.IntegerField(choices=[(3, '按钮'), (1, '菜单'), (2, '页面')], default=1),
        ),
    ]