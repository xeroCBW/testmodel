from django.db import models
from article.models import Post

from article.basemodels import BaseModel
class Comment(BaseModel):

    STATUS_NORMAL = 1
    STATUS_DELETE = 0

    COMMENT_TYPE = (
        (STATUS_NORMAL, '删除'),
        (STATUS_DELETE, '正常'),
    )

    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_content')
    email = models.EmailField()
    website = models.URLField()
    status = models.IntegerField(default = STATUS_NORMAL,choices=COMMENT_TYPE)

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.name