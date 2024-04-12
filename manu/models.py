from django.db import models

# Create your models here.
class categorydb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    details = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to="images",null=True,blank=True)

class itemdb(models.Model):
    cname = models.CharField(max_length=100,null=True,blank=True)
    iname = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    details = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(max_length=100,null=True,blank=True)
    image1 = models.ImageField(upload_to="images",null=True,blank=True)
