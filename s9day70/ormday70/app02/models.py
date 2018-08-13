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
    detail = models.OneToOneField(to="AuthorDetail")

    def __str__(self):
        return self.name


# 手动创建第三张作者和书相关联的表
# 此时在ORM层面上，作者和书没有多对多的关系了
class Author2Book(models.Model):
    id = models.AutoField(primary_key=True)

    # 作者id
    author = models.ForeignKey(to="Author")

    # 书id
    book = models.ForeignKey(to="Book")

    # 建立唯一约束
    class Meta:
        # 顺序不能变
        unique_together = ("author", "book")


class AuthorDetail(models.Model):
    bobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)
