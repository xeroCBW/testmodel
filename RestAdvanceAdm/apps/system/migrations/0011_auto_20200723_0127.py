# Generated by Django 2.2.5 on 2020-07-23 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20200721_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='type',
            field=models.IntegerField(choices=[(3, '按钮'), (1, '菜单'), (2, '页面')], default=1),
        ),
    ]
