# Generated by Django 2.2.5 on 2020-07-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20200721_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='type',
            field=models.IntegerField(choices=[(3, '按钮'), (2, '页面'), (1, '菜单')], default=1),
        ),
    ]
