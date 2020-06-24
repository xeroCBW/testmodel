from django.utils import timezone as datetime
from django.db import models


class BaseModel(models.Model):

    create_user = models.IntegerField(verbose_name="创建人",null=True, blank=True,help_text='创建者')
    create_time = models.DateTimeField("创建时间",default=datetime.now,help_text='创建时间')

    update_user = models.IntegerField(verbose_name="修改人",null=True, blank=True,help_text='修改者')
    update_time = models.DateTimeField("修改时间", default=datetime.now,help_text='修改时间')

    is_delete= models.BooleanField(default=False,verbose_name='逻辑删除',help_text='是否删除')

    # 级联删除会遇到一些问题
    # def delete(self, using=None, keep_parents=False):
    #     self.is_delete = True
    #     self.save()

    class Meta:
        abstract = True
    pass