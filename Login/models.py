from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    userid = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,default="anything")
    city=models.CharField(max_length=10,default="nadiad")
    mob = models.IntegerField()
    email = models.EmailField()
    usertype=models.CharField(max_length=10,default="Farmer")
# Create your models here.
