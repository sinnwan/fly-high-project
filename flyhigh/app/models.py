from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class LoginUser(AbstractUser):

    statuschoices=(('APPROVE','APPROVE'),
                   ('REJECT','REJECT'),
                   )
    status=models.CharField(choices=statuschoices,max_length=20,default='PENDING',null=True,blank=True)
    usertype=models.CharField(max_length=50,null=True,blank=True)

class user(models.Model):
    login_id=models.ForeignKey(LoginUser,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone_no=models.IntegerField()
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.user_name


class company(models.Model):
    login_id=models.ForeignKey(LoginUser,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone_no=models.IntegerField()
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.company_name

