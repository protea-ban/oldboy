from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    province = models.CharField(max_length=32)
    salary = models.IntegerField()
    dept = models.CharField(max_length=32)

    class Meta:
        db_table = 'employee'


class Employee2(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    province = models.CharField(max_length=32)
    salary = models.IntegerField()
    dept_id = models.ForeignKey(to="Dept2")
    
    class Meta:
        db_table = 'employee2'
        

class Dept2(models.Model):
    name = models.CharField(max_length=32)
    
    class Meta:
        db_table = 'dept2'


class Author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to="Book")
    
    class Meta:
        db_table = 'author'
        
        
class Book(models.Model):
    title = models.CharField(max_length=32)
    
    class Meta:
        db_table = 'book'
