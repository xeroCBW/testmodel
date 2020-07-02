# Generated by Django 2.2.5 on 2020-07-02 04:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_secret',
            field=models.UUIDField(default=uuid.UUID('10560746-cda8-47bf-ac9a-0137330f3140'), verbose_name='用户JWT秘钥'),
        ),
    ]
