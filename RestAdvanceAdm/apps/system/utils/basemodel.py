from django.db import models


class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # create_user = models.IntegerField(null=True,blank=True)
    # update_user = models.IntegerField(null=True,blank=True)