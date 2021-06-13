from django.db import models

# Create your models here.
class Userreg(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    class Meta:
        db_table="users"

class Pay(models.Model):
    reason=models.CharField(max_length=100)
    rupee=models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
   

class Addpost(models.Model):
    reason=models.CharField(max_length=100)
    count=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    caption=models.CharField(max_length=100)
    class Meta:
        db_table="post"

