from django.contrib import admin
from Xadmin.service.Xadmin import site
from .models import *

# Register your models here.
site.register(Book)
site.register(Author)
site.register(Publish)
site.register(AuthorDetail)
