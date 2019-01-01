from django.contrib import admin
from api import models

"""
superuser:root root1111
"""
# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.CourseDetail)
admin.site.register(models.Chapter)
admin.site.register(models.UserInfo)
admin.site.register(models.PricePolicy)
