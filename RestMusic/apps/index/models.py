from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    adress = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)
    create_time = models.DateTimeField('评论时间',null=True,blank=True, auto_now_add=True)


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Label(models.Model):

    name = models.CharField('分类列表',max_length=10)
    create_time = models.DateTimeField('评论时间',null=True,blank=True, auto_now_add=True)

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
    create_time = models.DateTimeField('评论时间',blank=True,null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Dynamic(models.Model):

    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')

    play_num = models.IntegerField('播放次数')
    search_num = models.IntegerField('搜索次数')
    down_num = models.IntegerField('下载次数')
    create_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

class Comment(models.Model):

    text = models.CharField('评论',max_length=500)
    # 删除的时候不做任何事情
    user = models.ForeignKey(UserProfile,verbose_name='评论用户',max_length=20,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')
    create_time = models.DateTimeField('评论时间',null=True,blank=True,auto_now_add=True)

