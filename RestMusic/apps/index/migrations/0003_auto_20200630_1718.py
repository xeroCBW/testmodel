# Generated by Django 2.0.2 on 2020-06-30 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200630_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_comment', to='index.Song', verbose_name='歌名'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL, verbose_name='评论用户'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='song',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='song_dynamic', to='index.Song', verbose_name='歌名'),
        ),
        migrations.AlterField(
            model_name='label',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='song',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='song',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='label_song', to='index.Label', verbose_name='歌曲分类'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
    ]
