import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ormday71.settings")

    import django
    django.setup()

    from app01 import models
    from django.db.models import Avg

    # 在一个表中进行分组查询
    # ret = models.Employee.objects.values("dept").annotate(avg=Avg("salary")).values("dept", "avg")
    # print(ret)

    # 在两个表中进行分组查询
    # ret = models.Employee2.objects.values("dept_id").annotate(avg=Avg("salary")).values("dept_id__name", "avg")
    # print(ret)

    # 两个表，查询员工姓名和部门名称
    # ret = models.Employee2.objects.values("name", "dept_id__name")
    # print(ret)

    # 两个表，查询员工姓名和部门名称的另一种方法
    # 通过select_related 函数将两张表连接一起
    # ret = models.Employee2.objects.select_related().values("name", "dept_id__name")
    # print(ret)

    # select_related函数也可以用在多对多的表上
    # ret = models.Author.objects.select_related("books__title").values("name", "books__title")
    # print(ret)

    # prefetch_related函数与select_related函数相同，速度更快
    # ret = models.Author.objects.prefetch_related("books__title").values("name", "books__title")
    # print(ret)

    # 批量操作，重点是bulk_crate函数
    objs = [models.Book(title="沙河{}".format(i)) for i in range(1000)]
    models.Book.objects.bulk_create(objs)

    # models.Book.objects.all().delete()

