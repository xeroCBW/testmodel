import django_filters
from system.models import Good, Button, Role, Page, UserProfile,Patent


class GoodFilter(django_filters.rest_framework.FilterSet):


    class Meta:
        model = Good
        fields = ['is_new','is_hot',]

class RoleFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Role
        fields = ['id',]

class PageFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Page
        fields = ['id',]

class ButtonFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Button
        fields = ['id',]


class UserFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = UserProfile
        fields = ['id','gender','name']

class PatentFilter(django_filters.rest_framework.FilterSet):
    # document_no = models.CharField(max_length=100, null=True, blank=True, help_text='文献号', verbose_name='文献号')
    # apply_no = models.CharField(max_length=100, null=True, blank=True, help_text='申请号', verbose_name='申请号')
    # apply_time = models.CharField(max_length=100, null=True, blank=True, help_text='申请时间', verbose_name='申请时间')
    # public_no = models.CharField(max_length=100, null=True, blank=True, help_text='公开号', verbose_name='公开号')
    # public_time = models.CharField(max_length=100, null=True, blank=True, help_text='公开时间', verbose_name='公开时间')
    #
    # name = models.CharField(max_length=100, null=True, blank=True, help_text='名称', verbose_name='名称')
    # apply_user = models.CharField(max_length=100, null=True, blank=True, help_text='申请用户', verbose_name='申请用户')
    # address = models.CharField(max_length=100, null=True, blank=True, help_text='申请人地址', verbose_name='申请人地址')
    # inventor = models.CharField(max_length=100, null=True, blank=True, help_text='发明者', verbose_name='发明者')
    # priority = models.CharField(max_length=100, null=True, blank=True, help_text='优先级', verbose_name='优先级')
    # category_no = models.CharField(max_length=100, null=True, blank=True, help_text='分类号', verbose_name='分类号')
    # main_category_no = models.CharField(max_length=100, null=True, blank=True, help_text='主要分类号', verbose_name='主要分类号')
    # nation_province = models.CharField(max_length=100, null=True, blank=True, help_text='国家省份', verbose_name='国家省份')
    #
    # internation_publish = models.CharField(max_length=100, null=True, blank=True, help_text='国际发布', verbose_name='国际发布')
    #
    # internation_publish_time = models.CharField(max_length=100, null=True, blank=True, help_text='国际发布时间',
    #                                             verbose_name='国际发布时间')
    #
    # phrator_date = models.CharField(max_length=100, null=True, blank=True, help_text='同族', verbose_name='同族')
    # quote_number = models.IntegerField(default=0, help_text='被引用数量', verbose_name='被引用数量')
    # quote_patent = models.CharField(max_length=100, null=True, blank=True, help_text='引用专利', verbose_name='引用专利')
    # abstract = models.CharField(max_length=1024, null=True, blank=True, help_text='摘要', verbose_name='摘要')
    # abstract_pic = models.CharField(max_length=100, null=True, blank=True, help_text='摘要图片', verbose_name='摘要图片')

    class Meta:
        model = Patent
        fields = ['id','document_no','apply_no','public_no','apply_user','inventor','category_no','main_category_no']