from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Menu(models.Model):
    """
    菜单
    """
    title = models.CharField(max_length=32, unique=True, verbose_name="菜单名")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父菜单",on_delete=models.CASCADE)
    is_top = models.BooleanField(default=False, verbose_name="首页显示")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码")
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)

    def __str__(self):
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    @classmethod
    def getMenuByRequestUrl(self, url):
        ret = dict(menu=Menu.objects.get(url=url))
        return ret


class Role(models.Model):
    """
    角色：绑定权限
    """
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField("menu",null=True, blank=True,default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

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
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg", max_length=100, null=True,
                              blank=True)
    department = models.ForeignKey("Structure", null=True, blank=True, verbose_name="部门",on_delete=models.CASCADE)
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")
    superior = models.ForeignKey("self", null=True, blank=True, verbose_name="上级主管",on_delete=models.CASCADE)
    roles = models.ManyToManyField("system.Role", verbose_name="角色", blank=True)
    joined_date = models.DateField(null=True, blank=True, verbose_name="入职日期")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Structure(models.Model):
    """
    组织架构
    """
    type_choices = (("firm", "公司"), ("department", "部门"))
    title = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department", verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类架构",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title