# Generated by Django 2.2.5 on 2020-07-03 20:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20200703_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='page_list',
        ),
        migrations.AddField(
            model_name='role',
            name='page_list',
            field=models.ManyToManyField(related_name='page_role', to='system.Page'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_secret',
            field=models.CharField(default=uuid.UUID('7ad112de-da4e-46f0-a92e-a50f7d861cba'), max_length=500, verbose_name='用户JWT秘钥'),
        ),
    ]
