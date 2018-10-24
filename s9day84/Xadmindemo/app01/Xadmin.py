from django.contrib import admin
from Xadmin.service.Xadmin import site, ModelXadmin
from .models import *
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse


class BookConfig(ModelXadmin):

    def edit(self, obj=None, is_header=False):

        # 用在传表头的时候
        if is_header is True:
            return "操作"

        url = reverse('change', args=(obj.pk, ))
        return mark_safe('<a href="'+url+'">编辑</a>')

    def delete(self, obj=None, is_header=False):

        # 用在传表头的时候
        if is_header is True:
            return "操作"

        url = reverse('delete', args=(obj.pk,))
        return mark_safe('<a href="'+url+'">删除</a>')

    def check(self, obj=None, is_header=False):

        # 用在传表头的时候
        if is_header is True:
            return "操作"

        return mark_safe('<input type="checkbox">')

    list_display = [check, "nid", "title", "price", "publish", edit, delete]


# Register your models here.
site.register(Book, BookConfig)
site.register(Author)
site.register(Publish)
site.register(AuthorDetail)
