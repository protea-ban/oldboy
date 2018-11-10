from django.contrib import admin
from Xadmin.service.Xadmin import site, ModelXadmin
from .models import *
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from django.forms import ModelForm
from django.forms import widgets as wid


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        labels={
            "title":"书籍名称",
            "price":"价格"
        }
        error_messages ={

        }


class BookConfig(ModelXadmin):
    list_display_links = ["title"]
    list_display = ["nid", "title", "price", "publish"]
    modelform_class = BookModelForm
    search_fields = ["title", "price"]

    def patch_init(self, request, queryset):
        queryset.update(price=123)

    patch_init.short_description = "批量初始化"

    actions = [patch_init]


# Register your models here.
site.register(Book, BookConfig)
site.register(Author)
site.register(Publish)
site.register(AuthorDetail)
