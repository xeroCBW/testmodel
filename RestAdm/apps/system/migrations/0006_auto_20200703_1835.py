# Generated by Django 2.2.5 on 2020-07-03 18:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20200702_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '页面',
                'verbose_name_plural': '页面',
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='role',
            name='menu_list',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_secret',
            field=models.CharField(default=uuid.UUID('166751ca-bbb8-48de-bfce-da1d0f08f7f2'), max_length=500, verbose_name='用户JWT秘钥'),
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_button', to='system.Page')),
            ],
            options={
                'verbose_name': '按钮',
                'verbose_name_plural': '按钮',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RolePageButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Button')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Page')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Role')),
            ],
            options={
                'unique_together': {('role', 'page', 'button')},
            },
        ),
    ]