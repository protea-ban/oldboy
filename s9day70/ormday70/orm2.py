import os
import sys

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday70.settings")
    import django

    django.setup()

    from app01 import models

    # 查找所有书名里包含沙河的书
    ret = models.Book.objects.filter(title__contains="沙河")
    print(ret)

    # 查找所有出版日期是2018年的书
    ret = models.Book.objects.filter(publish_date__year=2018)
    print(ret)

    # 查找价格大于10元的书
    ret = models.Book.objects.filter(price__gt=10)
    print(ret)

    # 找到在沙河的出版社
    ret = models.Publisher.objects.filter(city="沙河")
    print(ret)

    # distinct
    # 查所有书关联的出版社
    ret = models.Book.objects.all().values_list("publisher__name")
    print(ret)
    # distinct去重
    print(ret.distinct())

    # 将所有的书按照价格倒叙排序
    # 默认排序
    ret = models.Book.objects.all().order_by("price")
    print(ret)
    # 倒序
    print(ret.reverse())
    # 同时，支持使用减号表示倒序排序
    ret = models.Book.objects.all().order_by("-price")
    print(ret)

    # 查询书名是沙河异闻录的书的出版社的city
    ret = models.Book.objects.filter(title="沙河异闻录").values_list("publisher__city")
    print(ret)

    # 查询书名是沙河异闻录的书的作者的爱好（夸两张表）
    ret = models.Book.objects.filter(title="沙河异闻录").values("authors__detail__bobby")
    print(ret)

