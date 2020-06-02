from django.db import models

# Create your models here.


class Province(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class City(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)


class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City,on_delete=models.CASCADE)