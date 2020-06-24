# Generated by Django 2.0.2 on 2020-06-24 07:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200623_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['-id'], 'verbose_name': '角色表'},
        ),
        migrations.AlterModelOptions(
            name='structure',
            options={'ordering': ['-id'], 'verbose_name': '组织架构', 'verbose_name_plural': '组织架构'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'ordering': ['-id'], 'verbose_name': '用户角色中间表', 'verbose_name_plural': '用户角色中间表'},
        ),
        migrations.AddField(
            model_name='menu',
            name='roles',
            field=models.ManyToManyField(through='system.RoleMenu', to='system.Role'),
        ),
        migrations.AddField(
            model_name='role',
            name='peoples',
            field=models.ManyToManyField(through='system.UserRole', to=settings.AUTH_USER_MODEL),
        ),
    ]
