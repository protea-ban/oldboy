from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 创建一个自增的主键字段
    id = models.AutoField(primary_key=True)
    # 创建一个varchar(20)类型的字段
    name = models.CharField(max_length=20, null=False)