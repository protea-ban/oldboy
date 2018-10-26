from django.contrib import admin
from .models import *
# Register your models here.

class PerConfig(admin.ModelAdmin):
    list_display = ["title","url","group","action"]

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission,PerConfig)
admin.site.register(PermissionGroup)
