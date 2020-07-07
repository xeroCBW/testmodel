# Generated by Django 2.2.5 on 2020-07-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20200707_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemodel',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='basemodel',
            name='update_user',
        ),
        migrations.AlterField(
            model_name='permission',
            name='type',
            field=models.IntegerField(choices=[(1, '菜单'), (2, '页面'), (3, '按钮')], default=1),
        ),
    ]
