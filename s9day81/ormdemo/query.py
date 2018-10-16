#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: query.py 
@time: 2018/10/16
@software: PyCharm  
"""  
import os
import sys
import django
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormdemo.settings")
    django.setup()

    from app01 import models

    ####################基于对象查询######################
    # python_book = models.Book.objects.filter(title="python").first()
    # publish_obj = models.Publish.objects.filter(nid=python_book.publish_id).first()
    # print(publish_obj.email)
    # print(python_book.publish.email)

    # publish_obj=models.Publish.objects.filter(name="alex出版社").first()
    # for obj in publish_obj.book_set.all():
    #     print(obj.title)

    # python = models.Book.objects.filter(title="python").first()
    # for author_obj in python.authors.all():
    #     print(author_obj.age)

    # author_obj = models.Author.objects.filter(name="alex").first()
    # for book_obj in author_obj.book_set.all():
    #     print(book_obj.title)

    # author_obj = models.Author.objects.filter(name="alex").first()
    # print(author_obj.authorDetail.telephone)

    # auth_obj = models.AuthorDetail.objects.filter(addr="beijing").first()
    # print(auth_obj.author.name)

    ####################基于queryset和__查询（join查询）############
    # ret = models.Book.objects.filter(title="python").values("publish__email")
    # print(ret)

    # ret = models.Publish.objects.filter(name="alex出版社").values("book__title")
    # print(ret)

    ret = models.Book.objects.filter(authors__authorDetail__telephone__startswith="11").values("title","publish__name")
    print(ret)