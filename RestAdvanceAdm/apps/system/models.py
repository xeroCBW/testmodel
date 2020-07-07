from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from .utils.basemodel import BaseModel




class ButtonType(BaseModel):

    name = models.CharField(max_length=100,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '按钮'


    def __str__(self):

        return self.name



class Permission(BaseModel):

    TYPE_CHOICES = {
        (1,'菜单'),
        (2,'页面'),
        (3,'按钮'),
    }

    name = models.CharField(max_length=100,null=True,blank=True)
    code = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    parent_id = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_permission')
    order_num = models.IntegerField(default=0)
    icon = models.CharField(max_length=100,null=True,blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES,default=1)
    perms = models.CharField(max_length=500,blank=True,null=True)

    # check_all = models.BooleanField(default=False)
    # actionsOption = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub_actionsOption')

    is_top = models.BooleanField(default=False)


    class Meta:

        verbose_name='权限'

    def __str__(self):
        '''

        :return: 权限的层次菜单
        '''

        # return self.name
        # return '%s %s' %(self.parent_id.name if self.parent_id else '',self.name)
        return self.cadena()

    def cadena(self):
        if self.parent_id is None:
            return self.name
        else:
            return self.parent_id.cadena() + ' - ' + self.name





class Role(BaseModel):

    name = models.CharField(max_length=100,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    permission = models.ManyToManyField(Permission,related_name='permission_roles')

    class Meta:
        verbose_name = '角色'

    def __str__(self):
        return self.name


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

    roles = models.ManyToManyField(Role,related_name='role_users')

    avatar = models.ImageField(upload_to='avatar',null=True,blank=True)

    """用户模型类"""
    # user_secret = models.CharField(max_length=500,default=uuid4(), verbose_name='用户JWT秘钥')

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name



