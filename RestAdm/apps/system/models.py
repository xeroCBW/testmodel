from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


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

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name


class UserInfo(models.Model):

    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    add_time = models.DateTimeField("添加时间",default=datetime.now)
    class Mete:
        verbose_name = "用户信息表"
        ordering = ['-id']


class Role(models.Model):
    name = models.CharField(max_length=20,verbose_name="名称")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name='角色表'

        def __str__(self):
            return self.name

class Menu(models.Model):

    MENU_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(max_length=32, unique=True, verbose_name="菜单名")
    menu_type = models.IntegerField("类目级别", choices=MENU_TYPE, null=True, blank=True, help_text="类目级别")

    # 设置自己是自己的外键
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父菜单", on_delete=models.CASCADE,related_name="sub_menu")
    is_top = models.BooleanField(default=False, verbose_name="首页显示")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码")
    # 注意url不能重复
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)

    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name='菜单表'

        def __str__(self):
            return self.name


class Structure(models.Model):
    """
    组织架构
    """
    type_choices = (("firm", "公司"), ("department", "部门"))

    name = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department", verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类架构",on_delete=models.CASCADE,related_name='sub_structure')

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class UserRole(models.Model):

    role = models.ForeignKey(Role,on_delete=models.CASCADE,verbose_name='角色')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户')
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '用户角色中间表'
        verbose_name_plural = verbose_name
        unique_together = ('role','user')


class RoleMenu(models.Model):

    role = models.ForeignKey(Role,on_delete=models.CASCADE,verbose_name='角色')
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,verbose_name='菜单')
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '角色菜单中间表'
        verbose_name_plural = verbose_name
        unique_together = ('role','menu')




