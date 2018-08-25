from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


# class User(models.Model):
#     username = models.CharField(max_length=32, unique=True, null=True)
#     password = models.CharField(max_length=64, null=True)


class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=128)
