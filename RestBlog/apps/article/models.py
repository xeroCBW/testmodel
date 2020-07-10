from django.db import models
from django.contrib.auth.models import User

from .basemodels import BaseModel


class Category(BaseModel):

    STATUS_NORMAL = 1
    STATUS_DELETE = 0

    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL)
    is_nav = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.name

class Tag(BaseModel):

    STATUS_NORMAL = 1
    STATUS_DELETE = 0

    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Post(BaseModel):

    STATUS_DELETE = 0
    STATUS_NORMAL = 1
    STATUS_DRAFT = 2

    STATUS_ITEMS = (

        (STATUS_DELETE, '删除'),
        (STATUS_NORMAL, '正常'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1024)
    content = models.TextField()

    category = models.ForeignKey(Category,related_name='category_post',on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,related_name='tag_post')
    status = models.IntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Link(BaseModel):

    STATUS_DELETE = 0
    STATUS_NORMAL = 1


    STATUS_ITEMS = (

        (STATUS_DELETE, '删除'),
        (STATUS_NORMAL, '正常'),
    )

    name = models.CharField(max_length=127)
    href = models.URLField()# 默认长度200
    weight = models.IntegerField(default=STATUS_NORMAL)
    status = models.IntegerField(choices=STATUS_ITEMS,default=STATUS_NORMAL)

    class Meta:
        ordering = ['-id',]

    def __repr__(self):
        self.name

    def __str__(self):
        return self.name


class SliderBar(BaseModel):

    STATUS_HIDDEN = 0
    STATUS_NORMAL = 1

    STATUS_ITEMS = (

        (STATUS_HIDDEN, '隐藏'),
        (STATUS_NORMAL, '正常'),
    )


    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最新评论'),
    )

    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    type = models.PositiveIntegerField(default=1)
    status = models.IntegerField(default=STATUS_NORMAL)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name





