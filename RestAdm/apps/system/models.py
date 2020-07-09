from django.contrib.auth.models import AbstractUser
from django.db import models
from db_tools.base_model import *
from uuid import uuid4
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


class Page(BaseModel):

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '页面'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Button(BaseModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE,related_name='page_button')
    name = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']
        verbose_name = '按钮'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '(%s)%s' %(self.page.name,self.name)


class Role(BaseModel):

    name = models.CharField(max_length=20,verbose_name="名称")
    code = models.CharField(max_length=20,default='staff')

    # menu_list = models.ManyToManyField(Menu,related_name='role_list')

    page_list = models.ManyToManyField(Page,related_name='page_role')
    button_list = models.ManyToManyField(Button,related_name='button_role')

    class Meta:
        ordering = ['-id']
        verbose_name='角色表'

    def __str__(self):
        return self.name


    @classmethod
    def get_button_list_by_id(cls,role_id):
        '''

        :param role_id: 角色id
        :return: 返回角色下的所有按钮
        '''

        role = Role.objects.get(id=role_id)
        buttons = role.button_list.values('id','url','button_role').all()
        return buttons

    @classmethod
    def get_page_list_by_id(cls,role_id):
        '''

        :param role_id: 角色id
        :return: 返回角色下的所有页面
        '''
        role = Role.objects.get(id=role_id)
        roles = role.page_list.values('id', 'url', 'page_role').all()
        return roles


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

    roles = models.ManyToManyField(Role,related_name='user_list')

    avatar = models.ImageField(upload_to='avatar',null=True,blank=True)

    """用户模型类"""
    # user_secret = models.CharField(max_length=500,default=uuid4(), verbose_name='用户JWT秘钥')

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

class  AlbumImage(BaseModel):
    album = models.OneToOneField(Album,on_delete=models.CASCADE,related_name='album_image')
    image = models.ImageField(upload_to='album',null=True,blank=True,verbose_name='专辑图片',help_text='专辑图片')


    class Meta:
        verbose_name = '专辑图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 这里是返回用户的名字,本质是用户的图片
        return self.album.album_name



class Category(BaseModel):

    CATEGORY_TYPE = (
        (1,'一级类别'),
        (2,'二级类别'),
        (3,'三级类别')
    )
    name = models.CharField(max_length=100,verbose_name='标题',help_text='标题')
    # desc = models.CharField(max_length=1000,verbose_name='描述',help_text='描述')
    type = models.IntegerField(choices=CATEGORY_TYPE,default=1,verbose_name='类型',help_text='类型')
    code = models.CharField(max_length=100,verbose_name='编码',help_text='编码')
    is_top = models.BooleanField(default=False,verbose_name='是否是顶级菜单',help_text='是否是顶级菜单')
    # 设置foreignKey 一定要设置成自己
    parent_id = models.ForeignKey('self',default=None,null=True,blank=True,verbose_name='父菜单',help_text='父菜单',on_delete=models.CASCADE,related_name='sub_category')


    class Meta:
        ordering = ['-id']
        verbose_name='类别'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Good(BaseModel):


    category = models.ForeignKey(Category,on_delete=Category,default=None,null=True,blank=True,verbose_name='分类',help_text='分类',related_name='good_list')
    good_sn = models.IntegerField(null=True,blank=True,verbose_name='货物号',help_text='货物号')
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name='商品名',help_text='商品名')
    # desc = models.TextField(max_length=1000,null=True,blank=True,verbose_name='商品的描述',help_text='商品的描述')
    image = models.ImageField(null=True,blank=True,upload_to='goods',verbose_name='商品的主图片',help_text='商品的主图片')

    market_price = models.DecimalField(default=0.0,max_digits=20,decimal_places=3,verbose_name='市场的价格',help_text='市场的价格')
    shop_price = models.DecimalField(default=0.0, max_digits=20, decimal_places=3, verbose_name='本店的价格',help_text='本店的价格')

    click_num = models.IntegerField(default=0,verbose_name='点击次数',help_text='点击次数')
    favorate_num = models.IntegerField(default=0, verbose_name='喜欢次数', help_text='喜欢次数')
    sold_num = models.IntegerField(default=0, verbose_name='已卖数量', help_text='已卖数量')
    good_num = models.IntegerField(default=0, verbose_name='库存数量', help_text='库存数量')

    is_hot = models.BooleanField(default=False,verbose_name='商品是否热卖',help_text='商品是否热卖')
    is_new = models.BooleanField(default=False,verbose_name='是否新产品',help_text='是否新产品')

    ship_free = models.BooleanField(default=False,verbose_name='是否包邮',help_text='是否包邮')




    class Meta:
        ordering = ['-id']
        verbose_name='商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class UserFavorate(BaseModel):

    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户')
    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name='商品')

    class Meta:
        ordering = ['-id']
        unique_together = ("user", "good")
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.user.username



class Banner(BaseModel):

    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name='商品',help_text='商品',null=True,blank=True)
    image = models.ImageField(upload_to='banner',null=True,blank=True,verbose_name='图片',help_text='图片')
    index = models.IntegerField(default=1,verbose_name='轮播顺序',help_text='轮播顺序')


    class Meta:
        ordering = ['-id']
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.good.name


class Cart(BaseModel):

    good = models.ForeignKey(Good,on_delete=models.CASCADE,null=True,blank=True,help_text='商品',verbose_name='商品')
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True,help_text='用户',verbose_name='用户')
    num = models.IntegerField(verbose_name='商品数量',help_text='商品数量')

    class Meta:
        ordering = ['id']
        verbose_name='购物车'
        verbose_name_plural=verbose_name
        unique_together = ['good','user' ]

    def __str__(self):
        return '%s: %d' %(self.good.name,self.num)


class Order(BaseModel):

    PAY_TYPE = (
        (1,'微信'),
        (2,'支付宝'),
    )
    ORDER_STATUS = (
        ("paying", "待支付"),
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),

    )

    order_sn = models.CharField(max_length=100,null=True,blank=True,unique=True,verbose_name='订单号',help_text='订单号')

    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户',help_text='用户')
    pay_type = models.IntegerField(choices=PAY_TYPE,verbose_name='支付方式',default=1,help_text='支付方式')
    order_status = models.CharField(max_length=100,choices=ORDER_STATUS,default='paying',verbose_name='支付状态',help_text='支付状态')

    nonce_str = models.CharField(max_length=100,null=True,blank=True,verbose_name='微信订单号',help_text='微信订单号')
    trade_no = models.CharField(max_length=100, null=True, blank=True, verbose_name='支付宝订单号', help_text='支付宝订单号')

    order_num = models.DecimalField(max_digits=20,decimal_places=3,default=0.0,verbose_name='订单金额',help_text='订单金额')
    pay_time = models.DateTimeField(blank=True,null=True,help_text='支付时间',verbose_name='支付时间')
    post_script = models.TextField(max_length=200,null=True,blank=True,verbose_name='用户备注',help_text='用户备注')

    address = models.CharField(max_length=100,verbose_name='送货地址',help_text='送货地址')
    sign_name = models.CharField(max_length=30,verbose_name='收货人',help_text='收货人')
    sign_mobile = models.CharField(max_length=20,verbose_name='收货人电话',help_text='收货人电话')

    class Meta:
        ordering = ['-id']
        verbose_name = '订单'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.order_sn



class OrderGood(BaseModel):

    # 一个订单有多个货物
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='good_list')
    good = models.ForeignKey(Good,on_delete=models.CASCADE,)
    num = models.IntegerField(verbose_name='商品数量',default=0)

    class Meta:
        ordering = ['-id']
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn






#
# class RolePageButton(BaseModel):
#
#     role = models.ForeignKey(Role,on_delete=models.CASCADE)
#     page = models.ForeignKey(Page,on_delete=models.CASCADE)
#     button = models.ForeignKey(Button,on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ['role','page','button']
#
#     def __str__(self):
#         return "%s %s %s" %(self.role.name , self.page.name,self.button.name)

