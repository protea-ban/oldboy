from django.shortcuts import render
from app01 import models


# Create your views here.


def books(request):
    all_books = models.Book.objects.all()

    page_num = request.GET.get("pages")

    total_count = models.Book.objects.all().count()
    per_page = 10
    total_page, m = divmod(total_count, per_page)

    if m > 0:
        total_page += 1

    # 12. 实现对输入页码数非数字及超过总页码数的判断
    try:
        page_num = int(page_num)
        # 如果输入页码数过大，默认跳到最后一页
        if page_num > total_page:
            page_num = total_page
    except Exception as e:
        page_num = 1

    data_start = (page_num - 1) * 10
    data_end = page_num * 10

    page_books = all_books[data_start: data_end]

    # 1. 先实现一半一半
    max_page = 11
    # 10. 如果数据量少，页数也少
    if total_page < max_page:
        max_page = total_page
    half_max_page = max_page // 2
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page

    # 2. 特殊情况一：页码前面出现负值
    if page_start < 1:
        page_start = 1
        page_end = max_page

    # 3. 特殊情况二：页码后面出现空白页
    if page_end >= total_page:
        page_start = total_page - max_page + 1
        page_end = total_page

    page_html_list = []

    # 6. 前一页
    # page_html_list.append('<li><a href="/books/?pages={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num - 1))

    # 9. 解决在首页处点前一页
    if page_num == 1:
        page_html_list.append(
            '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
    else:
        page_html_list.append(
            '<li><a href="/books/?pages={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num - 1))

    # 4. 加上首页
    page_html_list.append('<li><a href="/books/?pages=1">首页</a></li>')

    for i in range(page_start, page_end + 1):
        # 11. 对当前页加上活动active样式类
        if i == page_num:
            temp = '<li class="active"><a href="/books/?pages={0}">{0}</a></li>'.format(i)
        else:
            temp = '<li><a href="/books/?pages={0}">{0}</a></li>'.format(i)
        page_html_list.append(temp)

    # 5. 加上尾页
    page_html_list.append('<li><a href="/books/?pages={0}">尾页</a></li>'.format(total_page))

    # 7. 加上后一页
    # page_html_list.append('<li><a href="/books/?pages={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num + 1))

    # 8. 解决最后一页时点后一页
    if page_num == total_page:
        page_html_list.append(
            '<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        page_html_list.append(
            '<li><a href="/books/?pages={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                page_num + 1))

    # 转成字符串
    page_html = "".join(page_html_list)

    return render(request, "books.html", {"books": page_books, "page_html": page_html})


def books2(request):
    all_books = models.Book.objects.all()
    page_num = request.GET.get("pages")
    page_num = int(page_num)
    data_start = (page_num - 1) * 10
    data_end = page_num * 10

    total_count = models.Book.objects.all().count()
    per_page = 10
    total_page, m = divmod(total_count, per_page)

    if m > 0:
        total_page += 1

    print(total_count)

    page_books = all_books[data_start: data_end]

    page_html_list = []

    for i in range(1, total_page+1):
        temp = '<li><a href="/books/?pages={0}">{0}</a></li>'.format(i)
        page_html_list.append(temp)

    # 转成字符串
    page_html = "".join(page_html_list)
    print(page_html)

    return render(request, "books.html", {"books": page_books, "page_html": page_html})


def depts(request):
    # 从相应模块中导入分页类
    from utils.myPage import myPage

    all_depts = models.Dept2.objects.all()
    page_num = request.GET.get("pages")
    total_num = models.Dept2.objects.all().count()

    # 实例化分页类
    page_obj = myPage(page_num, total_num, '/depts/', per_page=10, max_page=11)
    # 通过实例的变量从数据库中取出需要展示的数据
    ret = models.Dept2.objects.all()[page_obj.start:page_obj.end]
    # 由实例调用函数生成需要的HTML代码
    dept_page_html = page_obj.page_html()
    return render(request, "depts.html", {"depts": ret, "page_html": dept_page_html})
