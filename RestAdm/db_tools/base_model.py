from django.utils import timezone as datetime
from django.db import models


class BaseModel(models.Model):

    create_user = models.IntegerField(verbose_name="创建人",null=True, blank=True)
    create_time = models.DateTimeField("创建时间",default=datetime.now)

    update_user = models.IntegerField(verbose_name="修改人",null=True, blank=True)
    update_time = models.DateTimeField("修改时间", default=datetime.now)

    is_delete= models.BooleanField(default=False,verbose_name='逻辑删除')


    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()

    class Meta:
        abstract = True
    pass