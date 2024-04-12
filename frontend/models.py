from django.db import models

# Create your models here.
class contactdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    sub = models.CharField(max_length=100,null=True,blank=True)
    msg = models.CharField(max_length=200,null=True,blank=True)

class userdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    img = models.ImageField(upload_to="uimage",blank=True,null=True)

class cartdb(models.Model):
    qty = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True,blank=True)
    tprice = models.IntegerField(null=True,blank=True)
    uname = models.CharField(max_length=100,null=True,blank=True)
    pname = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="img",null=True,blank=True)

class wishlistdb(models.Model):
    pid = models.IntegerField(null=True,blank=True)
    cname = models.CharField(max_length=100,null=True,blank=True)
    uname = models.CharField(max_length=100,null=True,blank=True)
    iname = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    details = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(max_length=100,null=True,blank=True)
    image1 = models.ImageField(upload_to="images",null=True,blank=True)

class billdb(models.Model):
    uname = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    code = models.IntegerField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)