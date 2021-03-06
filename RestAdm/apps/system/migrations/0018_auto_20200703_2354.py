# Generated by Django 2.2.5 on 2020-07-03 23:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0017_auto_20200703_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='url',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_secret',
            field=models.CharField(default=uuid.UUID('4fe777b5-3586-45ff-a2ce-081754cff220'), max_length=500, verbose_name='用户JWT秘钥'),
        ),
    ]
