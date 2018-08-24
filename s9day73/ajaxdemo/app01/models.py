from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False)
    pwd = models.CharField(max_length=32, default="123456")
    email = models.CharField(max_length=32, null=True)
    mobile = models.CharField(max_length=11, null=True)
    city = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
