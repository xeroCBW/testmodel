from django.db import models

# Create your models here.


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20,default='请输入名称')

    def __str__(self):
        return self.type_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='请输入名称')
    weight = models.CharField(max_length=20,default='请输入weight')
    size = models.CharField(max_length=20,default='请输入尺寸')
    type = models.ForeignKey(Type,on_delete=models.CASCADE)