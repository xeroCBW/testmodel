from django.db import models


class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    # 设置成抽象
    class Meta:
        abstract = True