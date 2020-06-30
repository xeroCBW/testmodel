# Generated by Django 2.0.2 on 2020-06-30 16:09

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
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别')),
                ('adress', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y%m')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='评论')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间')),
            ],
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_num', models.IntegerField(verbose_name='播放次数')),
                ('search_num', models.IntegerField(verbose_name='搜索次数')),
                ('down_num', models.IntegerField(verbose_name='下载次数')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='分类列表')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='歌名')),
                ('singer', models.CharField(max_length=50, verbose_name='歌手')),
                ('time', models.CharField(max_length=10, verbose_name='时长')),
                ('ablum', models.CharField(max_length=50, verbose_name='专辑')),
                ('language', models.CharField(max_length=20, verbose_name='语种')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
                ('release', models.CharField(max_length=20, verbose_name='发行时间')),
                ('img', models.CharField(max_length=20, verbose_name='歌曲图片')),
                ('lyrics', models.CharField(default='暂无歌曲', max_length=50, verbose_name='歌词')),
                ('file', models.CharField(max_length=50, verbose_name='歌曲文件')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Label', verbose_name='歌曲分类')),
            ],
        ),
        migrations.AddField(
            model_name='dynamic',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名'),
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
    ]
