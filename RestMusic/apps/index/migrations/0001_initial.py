# Generated by Django 2.0.2 on 2020-06-30 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='评论')),
                ('user', models.CharField(max_length=20, verbose_name='评论用户')),
                ('date', models.CharField(max_length=50, verbose_name='评论时间')),
            ],
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_num', models.IntegerField(verbose_name='播放次数')),
                ('search_num', models.IntegerField(verbose_name='搜索次数')),
                ('down_num', models.IntegerField(verbose_name='下载次数')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='分类列表')),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Song', verbose_name='歌名'),
        ),
    ]
