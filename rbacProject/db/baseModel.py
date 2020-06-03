from django.db import models
from django.utils import timezone

class BaseModel(models.Model):

    create_user = models.CharField('创建用户',max_length=50)
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    update_user = models.CharField('更新用户',max_length=50)
    update_time = models.DateTimeField('更新时间',default=timezone.now)

    note = models.CharField('备注',max_length=200)
    status = models.IntegerField('状态',default=0,null=True, blank=True)

    class Meta:
        abstract = True