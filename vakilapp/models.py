from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Name=models.CharField(max_length=122)
    Email=models.CharField(max_length=122)
    Phone=models.CharField(max_length=20)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=1000)
    Date=models.DateField(null=True, default=None)

    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ['-id']
    
class Team_Member(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Image=models.ImageField(upload_to='Team_Photo')
    Name=models.CharField(max_length=122 ,null=True)
    Qualification=models.CharField(max_length=122 ,null=True)
    Description=models.CharField(max_length=1000 ,null=True)
    Email=models.CharField(max_length=122 ,null=True) 

    def __str__(self):
        return self.Name