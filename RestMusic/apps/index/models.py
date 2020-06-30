from django.db import models

# Create your models here.

class Label(models.Model):

    name = models.CharField('分类列表',max_length=10)
    def __str__(self):
        return self.name

class Song(models.Model):

    name = models.CharField('歌名',max_length=50)
    singer = models.CharField('歌手',max_length=50)
    time = models.CharField('时长',max_length=10)
    ablum = models.CharField('专辑',max_length=50)
    language = models.CharField('语种',max_length=20)
    type = models.CharField('类型',max_length=20)
    release = models.CharField('发行时间',max_length=20)
    img = models.CharField('歌曲图片',max_length=20)
    lyrics = models.CharField('歌词',max_length=50,default='暂无歌曲')
    file = models.CharField('歌曲文件',max_length=50)
    label = models.ForeignKey(Label,on_delete=models.CASCADE,verbose_name='歌曲分类')

    def __str__(self):
        return self.name

class Dynamic(models.Model):

    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')

    play_num = models.IntegerField('播放次数')
    search_num = models.IntegerField('搜索次数')
    down_num = models.IntegerField('下载次数')

class Comment(models.Model):

    text = models.CharField('评论',max_length=500)
    user = models.CharField('评论用户',max_length=20)
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')
    date = models.CharField('评论时间',max_length=50)

