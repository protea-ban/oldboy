from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# 导入 ModelForm
from django.forms import ModelForm
from django.forms import widgets as wid    # 避免重名


class Book(ModelForm):
    class Meta:
        # 对应的Model类
        model = models.Book
        # 字段，all表示列出所有字段
        fields = "__all__"

        # labels 自定义显示的名字，
        labels = {
            "title": "书名",
            "publish": "出版社",
            "date": "出版日期",
            "authors": "作者",
        }

        # error_messages用法：
        error_messages = {
            'title': {'required': "书名不能为空", },
            'date': {'required': "出版日期不能为空", },
        }

        # widgets用法,比如把输入用户名的input框给为Textarea
        widgets = {
            "title": wid.TextInput(attrs={"class": "form-control"}),
            "date": wid.TextInput(attrs={"type": "date"})
        }


# Create your views here.
def book(request):
    book_list = models.Book.objects.all()
    # book = Book()
    return render(request, 'book.html', locals())


def add_book(request):
    if request.method == "POST":
        book = Book(request.POST)
        if book.is_valid():
            book.save()
            return redirect('/book/')
    book = Book()
    return render(request, 'add.html', locals())


def edit_book(request, id):
    book_obj = models.Book.objects.filter(pk=id).first()
    if not book_obj:
        return HttpResponse("无该书籍")
    if request.method == "POST":
        book = Book(request.POST, instance=book_obj)
        if book.is_valid():
            book.save()
            return redirect('/book/')
    book = Book(instance=book_obj)
    return render(request, 'edit.html', locals())
