from django.contrib import admin
from Xadmin.service.Xadmin import site
from .models import *

# Register your models here.
site.register(Order)
site.register(Food)
print(site._registry)
