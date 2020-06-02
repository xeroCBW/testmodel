from django.db import models

# Create your models here.


class Type(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
