# Generated by Django 2.2.5 on 2020-07-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20200707_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='type',
            field=models.IntegerField(choices=[(2, '页面'), (3, '按钮'), (1, '菜单')], default=1),
        ),
    ]
