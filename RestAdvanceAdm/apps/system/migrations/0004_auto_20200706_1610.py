# Generated by Django 2.2.5 on 2020-07-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20200706_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='check_all',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permission',
            name='type',
            field=models.IntegerField(choices=[(2, '页面'), (3, '按钮'), (1, '菜单')], default=1),
        ),
    ]
