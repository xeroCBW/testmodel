from django.contrib.auth.models import AbstractUser
from django.db import models
from db_tools.base_model import *
# Create your models here.

# 这里不能同时存在 user 和 userprofile
# from django.contrib.auth import get_user_model
# User = get_user_model()

class Menu(BaseModel):

    MENU_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(max_length=32, unique=True, verbose_name="菜单名",help_text='菜单名')
    menu_type = models.IntegerField("类目级别", choices=MENU_TYPE, null=True, blank=True, help_text="类目级别")

    # 设置自己是自己的外键
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父菜单", on_delete=models.CASCADE,related_name="sub_menu",help_text='父菜单')
    is_top = models.BooleanField(default=False, verbose_name="首页显示",help_text='是否是顶级菜单')
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标",help_text='图标')
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码",help_text='编码')
    # 注意url不能重复
    url = models.CharField(max_length=128, unique=True, null=True, blank=True,help_text='url')

    class Meta:
        ordering = ['-id']
        verbose_name='菜单表'

    def __str__(self):
        return self.name + '(' + str(self.menu_type) + ')'



class Role(BaseModel):

    name = models.CharField(max_length=20,verbose_name="名称")

    menu_list = models.ManyToManyField(Menu,related_name='role_list')
    class Meta:
        ordering = ['-id']
        verbose_name='角色表'

    def __str__(self):
        return self.name



class Structure(BaseModel):
    """
    组织架构
    """
    type_choices = (("firm", "公司"), ("department", "部门"))

    name = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department", verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类架构",on_delete=models.CASCADE,related_name='sub_structure')

    class Meta:
        ordering = ['-id']
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 这里只是放用户的基本信息,有其他信息可以通过增加表来搞数据
class UserProfile(AbstractUser):
    """
    用户: makemigration提示错误：sers.UserProfile.user_permissions: (fields.E304)，
    需要在settings中指定自定义认证模型：AUTH_USER_MODEL = 'users.UserProfile'
    """
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("famale", "女")), default="male",
                              verbose_name="性别")
    mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    email = models.EmailField(max_length=100, verbose_name="邮箱")


    role_list = models.ManyToManyField(Role,related_name='user_list')

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name


class UserInfo(BaseModel):

    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = "用户信息表"



class UserAddress(models.Model):
    """
    用户收货地址
    """
    # 这个收货地址是一对多的关系
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户",related_name='user_address' )
    province = models.CharField("省份",max_length=100, default="")
    city = models.CharField("城市",max_length=100, default="")
    district = models.CharField("区域",max_length=100, default="")
    address = models.CharField("详细地址",max_length=100, default="")
    signer_name = models.CharField("签收人",max_length=100, default="")
    signer_mobile = models.CharField("电话",max_length=11, default="")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address



class UserMessage(BaseModel):


    MESSAGE_CHOICE = (
        (1,'留言'),
        (2,'投诉'),
        (3,'询问'),
        (4,'售后'),
        (5,'求购'),
    )

    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户',help_text='用户')
    message_type = models.IntegerField(default=1,choices=MESSAGE_CHOICE,verbose_name='留言类型',help_text='留言类型:(1,留言),(2,投诉),(3,询问),(4,售后),(5,求购)')
    subject = models.CharField(max_length=100,verbose_name='留言主题',help_text='留言主题')
    text = models.TextField(max_length=1000,default='',verbose_name='留言内容',help_text='留言内容')
    file = models.FileField(upload_to='message',verbose_name='上传的文件',help_text='上传的文件')


# 以下是测试demo

class Album(BaseModel):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.album_name

class Track(BaseModel):

    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField
    album = models.ForeignKey(Album,related_name='track_list',on_delete=models.CASCADE)

    class Meta:
        unique_together = ('album','order')
        ordering = ['order']

    def __str__(self):
        return '%d: %s' %(self.order,self.title)

class AlbumImage(BaseModel):

    album = models.OneToOneField(Album,on_delete=models.CASCADE,related_name='album_image')
    image = models.ImageField(upload_to='album',null=True,blank=True,verbose_name='专辑图片',help_text='专辑图片')


    class Meta:
        verbose_name = '专辑图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 这里是返回用户的名字,本质是用户的图片
        return self.album.album_name
