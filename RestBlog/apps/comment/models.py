from django.db import models
from article.models import Post

from article.basemodels import BaseModel
class Comment(BaseModel):


    COMMENT_TYPE = (
        (0, '删除'),
        (1, '正常'),
    )

    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_content')
    email = models.EmailField()
    website = models.URLField()
    type = models.IntegerField(default=1,choices=COMMENT_TYPE)