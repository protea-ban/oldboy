import os
import sys

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday70.settings")
    import django

    django.setup()

    # from app01 import models

    # 从app01中获取id为1的作者出的书
    # ret = models.Author.objects.get(id=1).books.all()
    # print(ret)

    # 移除作者所写书中id为1的书
    # models.Author.objects.get(id=1).books.remove(1)
    # ret = models.Author.objects.get(id=1).books.all()
    # print(ret)

    print("app02".center(80, "*"))
    from app02 import models
    # 在app02中查询作者id为1的书
    ret = models.Author2Book.objects.filter(author_id=1).values_list("book_id")

    # 1. 得到所对应的书的id
    ret = [i[0] for i in ret]

    # 2. 从book表中将对应id的书取出来
    ret = models.Book.objects.filter(id__in=ret)
    print(ret)

    print("app03".center(80, "*"))
    from app03 import models
    # 在app03中查询作者id为1的书
    # 操作过程其实跟app01当中的一样
    ret = models.Author.objects.get(id=1).books.all()
    print(ret)


