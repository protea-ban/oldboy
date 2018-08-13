from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    publisher = models.ForeignKey(to="Publisher")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.IntegerField()

    # 通过through和through_filed来指定自己创建的第三张表作为多对多的联系
    # 第一个字段：多对多设置在哪张表中，第三张表通过哪个字段找到这张表，就设置成这个字段
    books = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book"))

    detail = models.OneToOneField(to="AuthorDetail")

    def __str__(self):
        return self.name


class Author2Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(to="Author")
    book = models.ForeignKey(to="Book")

    memo = models.CharField(max_length=64, null=True)

    class Meta:
        unique_together = ("author", "book")


class AuthorDetail(models.Model):
    bobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)
