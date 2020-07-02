# Generated by Django 2.2.5 on 2020-07-02 08:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20200702_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_secret',
            field=models.CharField(default=uuid.UUID('f052d95c-2304-4177-ada4-20155cc5a2dd'), max_length=1000, verbose_name='用户JWT秘钥'),
        ),
    ]
