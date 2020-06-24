# Generated by Django 2.0.2 on 2020-06-24 11:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
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
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
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
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, help_text='修改时间', verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='逻辑删除')),
                ('name', models.CharField(help_text='菜单名', max_length=32, unique=True, verbose_name='菜单名')),
                ('menu_type', models.IntegerField(blank=True, choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', null=True, verbose_name='类目级别')),
                ('is_top', models.BooleanField(default=False, help_text='是否是顶级菜单', verbose_name='首页显示')),
                ('icon', models.CharField(blank=True, help_text='图标', max_length=50, null=True, verbose_name='图标')),
                ('code', models.CharField(blank=True, help_text='编码', max_length=50, null=True, verbose_name='编码')),
                ('url', models.CharField(blank=True, help_text='url', max_length=128, null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, help_text='父菜单', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='system.Menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '菜单表',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, help_text='修改时间', verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='逻辑删除')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('menu_list', models.ManyToManyField(related_name='role_list', to='system.Menu')),
            ],
            options={
                'verbose_name': '角色表',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, help_text='修改时间', verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='逻辑删除')),
                ('name', models.CharField(max_length=60, verbose_name='名称')),
                ('type', models.CharField(choices=[('firm', '公司'), ('department', '部门')], default='department', max_length=20, verbose_name='类型')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_structure', to='system.Structure', verbose_name='父类架构')),
            ],
            options={
                'verbose_name': '组织架构',
                'verbose_name_plural': '组织架构',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_user', models.IntegerField(blank=True, help_text='创建者', null=True, verbose_name='创建人')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_user', models.IntegerField(blank=True, help_text='修改者', null=True, verbose_name='修改人')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, help_text='修改时间', verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, help_text='是否删除', verbose_name='逻辑删除')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户信息表',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role_list',
            field=models.ManyToManyField(related_name='user_list', to='system.Role'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
