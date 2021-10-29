from django.db import models

# Create your models here.
class namedetail(models.Model):
    std_name=models.CharField(max_length=20)
    std_roll=models.IntegerField()
    std_sec=models.CharField(max_length=1)

class Person(models.Model):
    std_roll= models.IntegerField()
    location = models.CharField(max_length=10)
    phone= models.IntegerField()
    bld_grp= models.CharField(max_length=1)
    