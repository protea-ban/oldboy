from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, db_index=True)

    def __str__(self):
        return "我是一个{}对象".format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    # 价格
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)

    # 库存数
    kucun = models.IntegerField(default=1000)

    # 卖出数
    maichu = models.IntegerField(default=0)

    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE, db_constraint=False, related_name="books")

    def __str__(self):
        return "我是一本书{}".format(self.title)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to="Book")

class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    birthday = models.DateField(auto_now_add=True)

    def __str__(self):
        return "<Object:Person>{}".format(self.name)

    class Meta:
        ordering=("birthday", )