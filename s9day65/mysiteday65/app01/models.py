from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    addr = models.CharField(max_length=128, null=False)


# 书籍的类
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    # 创建该数据表中的外键，如果要关联的类在该类的上面，可以用to=类名，否则加上引号
    publisher = models.ForeignKey(to="Publisher")

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    # 该字段是实现作者表与书表多对多的关键，ORM自动创建第三张关联表。
    book = models.ManyToManyField(to="Book")