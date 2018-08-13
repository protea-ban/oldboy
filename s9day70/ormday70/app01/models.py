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
    books = models.ManyToManyField(to="Book", related_name="authors")
    detail = models.OneToOneField(to="AuthorDetail")

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    bobby = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)