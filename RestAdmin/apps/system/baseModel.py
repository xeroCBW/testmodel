from django.db import models


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    # 设置 abstract = True 来声明基表，作为基表的Model不会在数据库中形成对应的表
    class Meta:
        abstract = True