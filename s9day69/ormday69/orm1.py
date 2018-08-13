#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: orm1.py 
@time: 2018/08/04
@software: PyCharm  
"""  

import os

if __name__ == '__main__':
    # 导入配置环境,记不住就去manage.py中找
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday69.settings")
    # 启动Django
    import django
    django.setup()

    # 要进行的操作
    from app01 import models
    # 查询所有数据
    # print("all".center(60, "*"))
    # ret = models.Person.objects.all()
    # print(ret)
    #
    # # get 返回符合条件的对象，返回的结果只有一个
    # print("get".center(60, "*"))
    # ret = models.Person.objects.get(id=1)
    # print(ret)
    #
    # # filter 返回符合条件的对象，返回的结果只有一个
    # print("filter".center(60, "*"))
    # ret = models.Person.objects.filter()
    # print(ret[0])
    #
    # # exclude 返回符合条件的对象，返回的结果只有一个
    # print("exclude".center(60, "*"))
    # ret = models.Person.objects.exclude(id=1)
    # print(ret)
    #
    # # values 返回符合条件的对象，返回的结果只有一个
    # print("values".center(60, "*"))
    # ret = models.Person.objects.values()
    # print(ret)
    #
    # # values_list 返回符合条件的对象，返回的结果只有一个
    # print("values_list".center(60, "*"))
    # ret = models.Person.objects.values_list()
    # print(ret)
    #
    # # order_by 返回符合条件的对象，返回的结果只有一个
    # print("order_by".center(60, "*"))
    # ret = models.Person.objects.order_by()
    # print(ret)
    #
    # # reverse 返回符合条件的对象，返回的结果只有一个
    # print("reverse".center(60, "*"))
    # ret = models.Person.objects.reverse()
    # print(ret)
    #
    # # count 返回符合条件的对象，返回的结果只有一个
    # print("count".center(60, "*"))
    # ret = models.Person.objects.count()
    # print(ret)
    #
    # # first 返回符合条件的对象，返回的结果只有一个
    # print("first".center(60, "*"))
    # ret = models.Person.objects.first()
    # print(ret)
    #
    # # last 返回符合条件的对象，返回的结果只有一个
    # print("last".center(60, "*"))
    # ret = models.Person.objects.last()
    # print(ret)
    #
    # # exists 返回符合条件的对象，返回的结果只有一个
    # print("exists".center(60, "*"))
    # ret = models.Person.objects.exists()
    # print(ret)


    #__gt __lt
    # ret = models.Person.objects.filter(id__gt=2)
    # print(ret)

    # __contains __icontains
    # ret = models.Person.objects.filter(name__contains="小")
    # print(ret)
    #
    # # __in
    # ret = models.Person.objects.filter(id__in=[1, 2, 3])
    # print(ret)
    #
    # # __range
    # ret = models.Person.objects.filter(id__range=(1, 2))
    # print(ret)
    #
    # # date日期的应用 __year __month __day 多个表示且
    # ret = models.Person.objects.filter(birthday__day=6)
    # print(ret)


    # 外键查询
    # 正向查询
    # 1. 根据对象查询
    # book_obj = models.Book.objects.first()
    # publisher_obj = book_obj.publisher
    # ret = publisher_obj.id
    # print(ret)
    #
    # 2.根据双下划线跨表查询,双下划线就代表跨了一张表
    # ret = models.Book.objects.filter(id=1).values_list("publisher__name")
    # print(ret)

    # 反向查询
    # 1. 基于对象查询，
    # publisher_obj = models.Publisher.objects.first()
    # 表名__set
    # ret = publisher_obj.book_set.all()

    # 使用在models文件中对类进行related_name设置来代替 表名__set
    # ret = publisher_obj.books.all()
    # print(ret)
    #
    # # 2. 基于双下划线
    # ret = models.Publisher.objects.filter(id=1).values_list("books__title")
    # print(ret)

    # 多对多
    # 反向查询
    # author_obj = models.Author.objects.first()
    # ret = author_obj.books.all()
    # print(ret)

    # 1. create 创建
    # 通过作者创建了两本书，会自动保存
    # step1：在book表中创建了一本新书，step2：在作者和书的关系表中添加关联记录
    # author_obj.books.create(title="跟金老板学开坦克", publisher_id=2)

    # 2. add 添加
    # 添加对象
    # book_obj = models.Book.objects.get(id=7)
    # author_obj.books.add(book_obj)
    # 添加对象列表
    # book_objs = models.Book.objects.filter(id__gt=9)
    # author_obj.books.add(*book_objs)    # 要把列表打散再传进去

    # 直接添加id
    # author_obj.books.add(12)

    # 3. remove 删除
    # book_obj = models.Book.objects.get(title="跟金老板学开车")
    # author_obj.books.remove(book_obj)
    # 也可以直接传id
    # author_obj.books.remove(13)

    # 4. clear 清空
    # author_obj.books.clear()

    # 聚合
    from django.db.models import Avg, Sum, Max, Min, Count

    # 求平均价格 添加一个属性，默认为 字段名_函数名
    # ret = models.Book.objects.all().aggregate(price_avg=Avg("price"))
    # print(ret)

    # 求最大价格 ret是对象 通过 对象.属性 可以获得值 Min表示最小
    # ret = models.Book.objects.all().aggregate(price_max=Max("price"))
    # print(ret.get("price_max"))
    # print(ret)

    # 分组查询
    # 查询每一本书的作者个数
    # ret = models.Book.objects.all().annotate(author_num=Count("author"))
    # print(ret.author_num) # ret是列表，不能对其使用.属性
    # for book in ret:
    #     print("书名：{}，作者数量：{}".format(book.title, book.author_num))

    # 查询作者数量大于一的书
    # ret = models.Book.objects.all().annotate(author_num=Count("author")).filter(author_num__gt=1)
    # print(ret[0].title)

    # 查询各个作者出的书的总价格
    # ret = models.Author.objects.all().annotate(price_num=Sum("books__price")).values_list("name", "price_num")
    # ret = models.Author.objects.all().annotate(price_num=Sum("books__price")).values("name", "price_num")
    # print(ret.values_list("id", "name", "price_num"))
    # print(ret)
    # for i in ret:
    #     print(i.get("name"), i.get("price_num"))

    # F和Q
    # ret = models.Book.objects.filter(price__gt=9.99)
    # print(ret)

    # 查询库存数大于卖出数的所有书（两个字段作比较）
    from django.db.models import F
    # ret = models.Book.objects.filter(kucun__gt=F("maichu"))
    # for book in ret:
    #     print(book.title, book.kucun, book.maichu)

    # 刷单 把每一本书的卖出数都乘以3

    # 单个对象操作用save
    # obj = models.Book.objects.first()
    # obj.maichu = 100 * 3
    # obj.save()

    # 具体的对象没有 update(), QuerySet 对象才有 update() 方法
    # models.Book.objects.update(maichu=(F("maichu")+1)*3)

    # 给每一本书的书名后面加上 第一版
    # from django.db.models.functions import Concat
    # from django.db.models import Value
    #
    # models.Book.objects.update(title=Concat(F("title"), Value("第一版")))

    # Q查询
    from django.db.models import Q
    # 查询 卖出数大于1000，并且 价格小于100的所有书
    # ret = models.Book.objects.filter(maichu__gt=1000, price__lt=100)
    # print(ret)
    # 查询 卖出数大于1000，或者 价格小于100的所有书
    # ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=100))
    # print(ret)
    # Q查询和字段查询同时存在时， 字段查询要放在Q查询的后面
    ret = models.Book.objects.filter(Q(maichu__gt=1000) | Q(price__lt=100), title__contains="金老板")
    print(ret)
