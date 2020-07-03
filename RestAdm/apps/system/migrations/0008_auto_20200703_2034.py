# Generated by Django 2.2.5 on 2020-07-03 20:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20200703_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_secret',
            field=models.CharField(default=uuid.UUID('8a10dbdd-9719-4588-be5c-abead4b6e42f'), max_length=500, verbose_name='用户JWT秘钥'),
        ),
    ]
