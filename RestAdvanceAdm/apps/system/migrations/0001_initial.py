# Generated by Django 2.2.5 on 2020-07-06 14:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.BaseModel')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('order_num', models.IntegerField(default=0)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.IntegerField(choices=[(2, '页面'), (1, '菜单')], default=1)),
                ('perms', models.CharField(blank=True, max_length=500, null=True)),
                ('is_top', models.BooleanField(default=False)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Permission')),
            ],
            options={
                'verbose_name': '权限',
            },
            bases=('system.basemodel',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='system.BaseModel')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('permission', models.ManyToManyField(related_name='permission_roles', to='system.Permission')),
            ],
            options={
                'verbose_name': '角色',
            },
            bases=('system.basemodel',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(default='', max_length=20, verbose_name='姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('gender', models.CharField(choices=[('male', '男'), ('famale', '女')], default='male', max_length=10, verbose_name='性别')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='电话')),
                ('email', models.EmailField(max_length=100, verbose_name='邮箱')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('roles', models.ManyToManyField(related_name='role_users', to='system.Role')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]